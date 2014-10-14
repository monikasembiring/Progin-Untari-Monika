from xml.dom import minidom
import time
import urllib
import sys

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
print '====================================================='
rssupdated = 'Updated on ' + mychannel.getElementsByTagName('lastBuildDate')[0].childNodes[0].nodeValue
print rssupdated
print '====================================================='

itemlist = mychannel.getElementsByTagName('item')
itemlist.sort(key=lambda x: time.strptime(x.getElementsByTagName('pubDate')[0].childNodes[0].nodeValue, '%a, %d %b %Y %H:%M:%S %Z'), reverse=True)

i = 1
for s in itemlist :
	if i<=52 :
	#if s.getElementsByTagName('pubDate')[0].childNodes[0].nodeValue <= 'Tue, 14 Oct 2014 00:17:56 GMT' and s.getElementsByTagName('pubDate')[0].childNodes[0].nodeValue >= 'Mon, 13 Oct 2014 00:17:56 GMT' :
		itemtitle = s.getElementsByTagName('title')[0]
		print str(i) + '. ' + itemtitle.childNodes[0].nodeValue
		i = i+1 
		pubDate = s.getElementsByTagName('pubDate')[0]
		print '    Published on ' + pubDate.childNodes[0].nodeValue
		itemcontent = s.getElementsByTagName('description')[0]
		itemcontent = s.getElementsByTagName('guid')[0]
		print '    Link : ' + itemcontent.childNodes[0].nodeValue
		print ''
