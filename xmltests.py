__author__ = 'alex'
import csv
import xml.etree.ElementTree as ET
# import xml.etree.cElementTree as cET
from xml.dom import minidom

def prettify(elem):
    # Return a pretty-printed XML string for the Element.
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")


'''
To do:
- Must do: add all conversion and transformation from input to XML
- Must do: add a configuration file or constants for required IDs
- Nice to have: add a switch for the nodes type and action to allow for more than one kind of node and actions.
- Nice to have: use the column title to map with the nodes of the xml file?
'''

importTree = ET.Element("import")
with open('wallets_UTF8.csv', 'r') as csvFile:
    wallReader = csv.reader(csvFile, delimiter=',', quotechar='"')
    for row in wallReader:
        node = ET.SubElement(importTree,"node", type="physicalitem", action="create")
        ET.SubElement(node,"location").text = row[1]
        ET.SubElement(node,"title").text = row[2]

# Removing first node as it only contains the column header:
first_node = importTree[0]
importTree.remove(first_node)

tree = ET.ElementTree(importTree)

print(prettify(importTree))
tree.write("filename.xml")