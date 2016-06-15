#!/urs/bin/python

import argparse
import xml.etree.ElementTree as ET

parser = argparse.ArgumentParser(description='Parse XML and save correct data to database')
parser.add_argument('inputf', metavar='<Input File>', type=str, help='input file')
parser.add_argument('--outputf', metavar='<Output File>', type=str, help='output file')
parser.add_argument('--path', type=str, help='Assing path to root element where program starts searching for keys. Syntax: parent/child/grandchild. If not defined, document root used as root element.')
parser.add_argument('--keys', type=str, nargs='*', help='Define key values.')

# parse args
args = parser.parse_args()

# define search keys
keys = args.keys

# define nodes
path = args.path
nodes = []
index = 0
for i in range(0, len( path )-1):
	if path[i] == '/':
		nodes.append(path[index:i])
		index=i+1
nodes.append(path[index:len( path )])
print(nodes)

# parse input and output files and print to conlose
print("Input file: ", args.inputf)
if args.outputf is not None:	
	print("Output file: ", args.outputf)

# parse tree from xml
tree = ET.parse(args.inputf)
root = tree.getroot()

document = root.find("documents")

for child in document:
	print(child.tag, ":", child.text)

print(args.keys)