from xml.dom import minidom
import urllib

url_str = 'http://feeds.bbci.co.uk/news/rss.xml?edition=int'
xml_str = urllib.urlopen(url_str).read()
xmldoc = minidom.parseString(xml_str)

item_values = xmldoc.getElementsByTagName('item')

for s in item_values:
	print s.childNodes[1].nodeName + " = " + s.childNodes[1].childNodes[0].nodeValue
	print s.childNodes[3].nodeName + " = " + s.childNodes[3].childNodes[0].nodeValue	
	print s.childNodes[9].nodeName + " = " + s.childNodes[9].childNodes[0].nodeValue
	
