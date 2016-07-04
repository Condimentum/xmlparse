#!/urs/bin/python

import argparse
import xml.etree.ElementTree as ET
import json

def main(inputf, keys, path):
	parser = argparse.ArgumentParser(description='XML parser')
	parser.add_argument('inputf', metavar='<Input File>', type=str, help='input file')
	parser.add_argument('keys', type=str, nargs='*', help='Define key values.')
	parser.add_argument('--path', type=str, help='Define path to root element where program starts searching for keys. Syntax: parent/child/grandchild. If not defined, document root used as root element.')
	
	# parse args
	args = parser.parse_args()
	
	# define search keys
	if args.keys is not None:
		keys = args.keys
	
	# define nodes
	if args.path is not None:
		path = "./" + args.path
	
	# define input file
	if args.inputf is not None:
		inputf = args.inputf
	
	# parse tree from xml
	tree = ET.parse(inputf)
	root = tree.getroot()
	dictList = []
	pairs = {}
	
	if args.path is not None:
		roots = root.findall(path)
	else:
		roots = []
		roots.append(root)
	
	# print("-----------------")
	# print("Found value, key pairs:")
	
	for r in roots:
		tmpdict = {}
		for key in keys:
			elements = r.findall(key)
			for e in elements:
				#print(e.tag, ":", e.text)
				tmpdict[e.tag] = e.text
		dictList.append(tmpdict)
	
	for d in dictList:
		for key in keys:
			print (key, ":", d[key])

if __name__ == "__main__":
    main('', '', '')