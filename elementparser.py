#!/urs/bin/python

import argparse
import xml.etree.ElementTree as ET
import json

parser = argparse.ArgumentParser(description='XML parser')
parser.add_argument('inputf', metavar='<Input File>', type=str, help='input file')
parser.add_argument('pairs', type=str, nargs="*", help='Define key-value pairs. Syntax: key1:value1 key2:value2')
parser.add_argument('--path', type=str, help='Define path to root element where program starts searching for child elements. Syntax: parent/child/grandchild. If not defined, document root used as root element.')

# parse args
args = parser.parse_args()

# define search keys and values
pairList = args.pairs
pairs = {}
for pairstr in pairList:
	i=0
	for char in pairstr:
		if char == ':':
			pairs[pairstr[:i]] = pairstr[i+1:]
			break
		i += 1

for key in pairs:
	print("key: ",key)
	print("value: ", pairs[key])
	print()

# define nodes
if args.path is not None:
	path = "./" + args.path

# parse tree from xml
tree = ET.parse(args.inputf)
root = tree.getroot()
dictList = []
elementList = []

if args.path is not None:
	roots = root.findall(path)
else:
	roots = []
	roots.append(root)

for r in roots:
	for child in r:
		for key in pairs:
			if child.tag == key and child.text == pairs[key]:
				ET.dump(r)
				break