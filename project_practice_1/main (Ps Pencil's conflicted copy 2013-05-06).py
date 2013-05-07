from flask import *
from functools import wraps
import sqlite3
import hashlib
import datetime
import re
DATABASE = "/home/pspencil/Dropbox/project_practice_1/model.db"

app = Flask(__name__)
app.config.from_object(__name__)

app.secret_key = 'Ps-PEncil'

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username','')
    flash('You were logged out')
    return redirect (url_for('login'))

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if not 'logged_in' in session:
        if request.method == 'POST':
            username=request.form['username']
            password=request.form['password']
            g.db=connect_db()
            cur=g.db.execute('select password from users where username = :1',[username]).fetchone()
            if not cur:
                error = 'User does not exist'
            elif hashlib.sha256(password).hexdigest()!=cur[0]:
                error = "Incorrect Password"
            else:
                session['logged_in'] = True
                session['username']=username
                g.db.close()
                return redirect(url_for('items'))
        return render_template('login.html', error=error)
    else:
        return redirect(url_for('items'))



@app.route('/signup',methods=['GET','POST'])
def signup():
    error=None
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        verify=request.form['verify']
        email=request.form['email']
        g.db=connect_db()
        cur=g.db.execute('select * from users where username= :1',[username]).fetchone()
        EMAIL_RE  = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
        if verify!=password:
            error="Passwords do not match!"
        elif cur:
            error="username already exists"
        elif not EMAIL_RE.match(email):
            error="Email format incorrect!"
        else:
            g.db.execute("insert into users VALUES(?,?,?)",[username,str(hashlib.sha256(password).hexdigest()),email])
            g.db.commit()
            g.db.close()
            session['logged_in']=True
            session['username']=username
            return redirect(url_for('items'))
    return render_template('signup.html',error=error)

@app.route('/items',methods=['GET','POST'])
@login_required
def items():
    error=None
    g.db=connect_db()
    cur=g.db.execute('select * from items where quantity > 0').fetchall()
    num=len(cur)
    if request.method=="GET":
        return render_template('item.html',items=cur,num_items=num,status="logout")
    if request.method=="POST":

        names=['A4 lecture pad', '7-colour sticky note with pen', 'A5 ring book', 'A5 note book with zip bag', '2B pencil', 'Stainless steel tumbler', 'A4 clear holder', 'A4 vanguard file', 'Name card holder', 'Umbrella', 'School badge (Junior High)', 'School badge (Senior High)', 'Dunman dolls (pair)']
        nicknames=['pad','note','book','bag','pencil','tumbler','holder', 'file', 'cardholder', 'umbrella', 'jhbadge', 'shbadge', 'doll']
        dictionary=dict()

        for i in range(0,len(names)):
            dictionary[names[i]]=nicknames[i]
        username=session['username']
        #orders=g.db.execute("select count(*) from orders where username = :1",username)
    
        total=float(request.form['total'])
        g.db.execute("insert into orders(username,total,'pad','note','book','bag','pencil','tumbler','holder', 'file', 'cardholder', 'umbrella', 'jhbadge', 'shbadge', 'doll') VALUES(?, ?,0,0,0,0,0,0,0,0,0,0,0,0,0)",[username,total])
        row_id=g.db.execute('SELECT MAX(id) FROM orders').fetchone()
        for i in range(0,num):
            qty=request.form[str(i)]
            if not qty:
                continue
            name=cur[i][0]
            #g.db.execute("update orders set "+dictionary[name]+" = "+str(qty)+" where id= "+str(row_id))
            g.db.execute("update orders set "+dictionary[name]+" = ? where id= ?",[int(qty),int(row_id[0])])


            left=g.db.execute('select quantity from items where name = ?',[name]).fetchone()[0]
            g.db.execute('update items set quantity=? where name=?',[int(left)-int(qty),name])

        g.db.commit()
        g.db.close()
        return redirect(url_for('items'))

@app.route('/myorders')
@login_required
def myorders():
    g.db=connect_db()
    cur=g.db.execute('select * from orders where username = ?',[session['username']]).fetchall()
    names=['A4 lecture pad', '7-colour sticky note with pen', 'A5 ring book', 'A5 note book with zip bag', '2B pencil', 'Stainless steel tumbler', 'A4 clear holder', 'A4 vanguard file', 'Name card holder', 'Umbrella', 'School badge (Junior High)', 'School badge (Senior High)', 'Dunman dolls (pair)']
    g.db.close()
    return render_template('orders.html',names=names,orders=cur,status="logout")


if __name__ == '__main__':
    app.run(debug=True)