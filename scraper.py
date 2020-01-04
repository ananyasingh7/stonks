import sys
import xml.dom.minidom
import csv

document = xml.dom.minidom.parse(sys.argv[1])







table = document.getElementsByTagName('table')
stockinfo = []
for b in table[3].getElementsByTagName('b'):
	for node in b.childNodes:
		if node.nodeType == node.TEXT_NODE:
			stockinfo.append(node.nodeValue)

print(stockinfo)
stockinfo[0] = stockinfo[0][1:]
stockinfo[1] = stockinfo[1][1:]
print(stockinfo)