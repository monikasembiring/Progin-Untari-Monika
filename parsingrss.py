from xml.dom import minidom
import time
import urllib
import sys
import datetime

if len(sys.argv) > 1:
	xmlurl = sys.argv[1]
	print 'Retrieving RSS feed from ' + xmlurl
	if xmlurl != '':
		testfile = urllib.URLopener()
		testfile.retrieve(xmlurl, "bbcrss.xml")

xmldoc = minidom.parse('bbcrss.xml')

mychannel = xmldoc.getElementsByTagName('channel')[0]
rsstitle = mychannel.getElementsByTagName('title')[0]
rssdesc = mychannel.getElementsByTagName('description')[0]

print ''
print rsstitle.childNodes[0].nodeValue + ' | ' + rssdesc.childNodes[0].nodeValue
print ''
print '-----------------------------------------------------'
rssupdated = 'Last 24 Hours News Updated on ' + mychannel.getElementsByTagName('lastBuildDate')[0].childNodes[0].nodeValue
print rssupdated
print '-----------------------------------------------------'

itemlist = mychannel.getElementsByTagName('item')
itemlist.sort(key=lambda x: time.strptime(x.getElementsByTagName('pubDate')[0].childNodes[0].nodeValue, '%a, %d %b %Y %H:%M:%S %Z'), reverse=True)

i = 1
for s in itemlist :
	pubTime = datetime.datetime.fromtimestamp(time.mktime(time.strptime(s.getElementsByTagName('pubDate')[0].childNodes[0].nodeValue, '%a, %d %b %Y %H:%M:%S %Z')))
	diffTime = (datetime.datetime.now() - pubTime)
	diffTime = diffTime.seconds + diffTime.days*24*60*60
	if diffTime <= 86400:
		itemtitle = s.getElementsByTagName('title')[0]
		print str(i) + '. ' + itemtitle.childNodes[0].nodeValue
		i = i+1 
		pubDate = s.getElementsByTagName('pubDate')[0]
		print '    Published on ' + pubDate.childNodes[0].nodeValue
		itemcontent = s.getElementsByTagName('description')[0]
		itemcontent = s.getElementsByTagName('guid')[0]
		print '    Link : ' + itemcontent.childNodes[0].nodeValue
		print ''
