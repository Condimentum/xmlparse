#!/urs/bin/python

import argparse
import xml.etree.ElementTree as ET
import json

def main(inputf, keys, path):
	parser = argparse.ArgumentParser(description='XML parser')
	parser.add_argument('inputf', metavar='<Input File>', type=str, help='input file')
	parser.add_argument('keys', type=str, nargs='*', help='Define key values.')
	parser.add_argument('--xpath', type=str, help='Define path to root element where program starts searching for keys. Syntax: parent/child/grandchild. If not defined, document root used as root element.')
	parser.add_argument('--output', type=str, help='Output file')
	# parse args
	args = parser.parse_args()
	
	# define search keys
	if args.keys is not None:
		keys = args.keys
	
	# define nodes
	if args.xpath is not None:
		path = "./" + args.xpath
	
	# define input file
	if args.inputf is not None:
		inputf = args.inputf

	if args.output is not None:
		outputf = args.output + ".json"

	parseValues(inputf, keys, path, outputf)

def parseValues(inputf, keys, path, outputf):
	
	# parse tree from xml
	tree = ET.parse(inputf)
	root = tree.getroot()
	dictList = []
	pairs = {}
	
	if path is not None:
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

	if outputf is not None:
		with open (outputf, 'w') as outfile:
			json.dump(dictList, outfile)
		print("Write to", outputf)

	return dictList

if __name__ == "__main__":
    main('', '', '')