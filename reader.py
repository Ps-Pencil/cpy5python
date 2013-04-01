from xml.dom import minidom
import re
import urllib2
import json

# get XML RSS feed
response = urllib2.urlopen("http://www.dhs.sg/rss/what%2527s-new%3F-19.xml")
xml = response.read()
outfile=open("feed.json","a")
# get all XML as a string
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
outfile.write(encoded)