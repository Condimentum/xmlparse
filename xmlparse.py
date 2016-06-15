#!/urs/bin/python

import argparse
import xml.etree.ElementTree as ET

parser = argparse.ArgumentParser(description='Parse XML and save correct data to database')
parser.add_argument('inputf', metavar='<Input File>', type=str, help='input file')
parser.add_argument('--outputf', metavar='<Output File>', type=str, help='output file')
parser.add_argument('--keys', type=str, nargs='*', help='Define key values.')
parser.add_argument('--path', type=str, help='Assing path to root element where program starts searching for keys. Syntax: parent/child/grandchild. If not defined, document root used as root element.')

# parse args
args = parser.parse_args()

# define search keys
if args.keys is not None:
	keys = args.keys
	print("keys:", keys)

# define nodes
if args.path is not None:
	path = "./" + args.path
	print("path: ", path)

# parse input and output files and print to conlose
print("Input file: ", args.inputf)
if args.outputf is not None:	
	print("Output file: ", args.outputf)

# parse tree from xml
tree = ET.parse(args.inputf)
root = tree.getroot()

roots = root.findall(path)

print("-----------------")
print("Found value, key pairs:")
for r in roots:
	for key in keys:
		elements = r.findall(key)
		for e in elements:
			print(e.tag, ":", e.text)