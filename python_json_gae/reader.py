from xml.dom import minidom
import re
import urllib2
import json
import os

import webapp2
import jinja2
from google.appengine.api import mail
from google.appengine.ext import db
from google.appengine.api import users


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)
def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

class BaseHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        return render_str(template, **params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))
class MainPage(BaseHandler):
    def get(self):
# get XML RSS feed
        page=self.request.get('page')
        if not page:
            page=1
        page=int(page)
        response = urllib2.urlopen("http://www.dhs.sg/rss/what%2527s-new%3F-19.xml")
        xml = response.read()
        #outfile=open("feed.json",'w')
        # get all XML as a parseString
        xml_data = minidom.parseString(xml).getElementsByTagName('channel')

# get all items
        parts = xml_data[0].getElementsByTagName('item')

        results=[]
# loop all items
        for part in parts:
    # get title
            title = part.getElementsByTagName('title')[0].firstChild.nodeValue.strip()
    # get link
            link = part.getElementsByTagName('link')[0].firstChild.nodeValue.strip()
    # get description
            description = part.getElementsByTagName('description')[0].firstChild.wholeText.strip()
            description = re.sub("<[^>]*>", "", description)
            description = description[:-10]
            result=dict(title=title,link=link,description=description)
            results.append(result)

        encoded=json.dumps(results,sort_keys=False,indent=2)
        #outfile.write(encoded)
        self.render("index.html",results=results[10*(page-1):10*page])



app = webapp2.WSGIApplication([('/', MainPage),
                                ],
                              debug=True)