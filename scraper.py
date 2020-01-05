import sys
import xml.dom.minidom
import csv

document = xml.dom.minidom.parse(sys.argv[1])

header = []

table = document.getElementsByTagName('table')
strong = document.getElementsByTagName('strong')
stockinfo = []
for b in table[3].getElementsByTagName('b'):
	for node in b.childNodes:
		if node.nodeType == node.TEXT_NODE:
			stockinfo.append(node.nodeValue)
for node in strong[0].childNodes:
	if node.nodeType == node.TEXT_NODE:
		name = node.nodeValue


stockinfo[0] = stockinfo[0][1:]
stockinfo[1] = stockinfo[1][1:]
print("------------------------------------------------")
print("COMPANY PROFILE: " + name)
print("LAST: " + stockinfo[0])
if stockinfo[2] > stockinfo[0]:
	print("CHANGE: +" + stockinfo[1])
else:
	print("CHANGE: -" + stockinfo[1])
print("OPEN: " + stockinfo[2])
print("PREV " + stockinfo[7])
print("HIGH: " + stockinfo[3])
print("LOW: " + stockinfo[8])
print("ASK: " + stockinfo[4])
print("BID: " + stockinfo[9])
print("VOLUME: " + stockinfo[5])
print("OPEN INT: " + stockinfo[10])