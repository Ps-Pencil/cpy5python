names=['A4 lecture pad', '7-colour sticky note with pen', 'A5 ring book', 'A5 note book with zip bag', '2B pencil', 'Stainless steel tumbler', 'A4 clear holder', 'A4 vanguard file', 'Name card holder', 'Umbrella', 'School badge (Junior High)', 'School badge (Senior High)', 'Dunman dolls (pair)']
nicknames=['pad','note','book','bag','pencil','tumbler','holder', 'file', 'cardholder', 'umbrella', 'jhbadge', 'shbadge', 'doll']
dictionary=dict()

for i in range(0,len(names)):
	dictionary[names[i]]=nicknames[i]
for name in names:
	print "update orders set "+dictionary[name]+" = "+'1'+" where id= "+'1'