import csv
import requests
import xml.etree.ElementTree as ET
import xml
from lxml import etree

def parseXML(xmlfile):
 
    # create element tree object
    tree = ET.parse(xmlfile)
 
    # get root element
    root = tree.getroot()
 
    # create empty list for news items
    newsitems = []
 
    # iterate news items
    for item in root.findall('./channel/item'):
 
        # empty news dictionary
        news = {}
 
        # iterate child elements of item
        for child in item:
 
            # special checking for namespace object content:media
            if child.tag == '{http://search.yahoo.com/mrss/}content':
                news['media'] = child.attrib['url']
            else:
                news[child.tag] = child.text.encode('utf8')
 
        # append news dictionary to news items list
        newsitems.append(news)
     
    # return news items list
    return newsitems


f = open('MeterReads2.xml', 'r').read()
#print f

ns = {'Header': 'http://iec.ch/TC57/2011/schema/message}Header', 
	  'Payload': 'http://iec.ch/TC57/2011/schema/message}Payload'}

#readings = {}

tree = etree.fromstring(f)

tree2 = ET.parse('MeterReads2.xml')
 
    # get root element
root2 = tree2.getroot()

#root = xml.etree.fromstring('MeterReads2.xml')
#ns = xml.etree.FunctionNameSpace('http://iec.ch/TC57/2011/schema/message')

ns = {'meter': 'http://iec.ch/TC57/2013/MeterReadings#', 'message':'http://iec.ch/TC57/2011/schema/message'}

print tree.findall('meter:MeterReading', ns)


# for i in tree:
# 	print i

# for i in root2:
# 	for j in i:
# 		print j
# 		for k in j:
# 			for z in k:
# 				print z[0].text, z.attrib, z.tag

			#print k

# for item in root2:
# 	print item.tag, item.attrib
# 	if 'Payload' in item:
# 		print 'hi'


	# for child in item:
	#  	#print child, child.tag
	# 	#if child.tag == '{http://iec.ch/TC57/2011/schema/message}Timestamp':
	# 	for z in child:
	# 		print z 




# get root element
#root = tree.getroot()


