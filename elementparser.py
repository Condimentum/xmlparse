#!/urs/bin/python

import argparse
import xml.etree.ElementTree as ET
import xml.dom.minidom as DOM
import time
import datetime

# for console output
removedElements = {}

def addToRemovedList(tag):
	if tag not in removedElements:
		removedElements[tag] = 1
	else:
		removedElements[tag] += 1

def main():
	# init parser
	parser = argparse.ArgumentParser(description='XML parser')
	parser.add_argument('inputf', metavar='<Input File>', type=str, help='input file')
	parser.add_argument('pairs', type=str, nargs="*", help='Define key-value pairs. Syntax: key1:value1 key2:value2')
	parser.add_argument('--xpath', type=str, help='Define path to root element where program starts searching for child elements. Syntax: parent/child/grandchild. If not defined, document root used as root element.')
	parser.add_argument('--output', type=str, help='Output file')
	
	# parse args
	args = parser.parse_args()
	
	# define search keys and values
	pairs = {}
	if args.pairs is not None:
		pairList = args.pairs
		for pairstr in pairList:
			i=0
			for char in pairstr:
				if char == ':':
					pairs[pairstr[:i]] = pairstr[i+1:]
					break
				i += 1
	
	# define nodes
	if args.xpath is not None:
		path = args.xpath
	else: path = ''
	
	# parse tree from xml
	if args.inputf is not None:
		inputf = args.inputf
	else: inputf=''

	if args.output is not None:
		outputf = args.output
	else: outpuf=''

	parseElements(inputf, pairs, path, outputf)

def parseElements(inputf, pairs, path, outputf):
	
	# print search parameters
	print("---Search parameters---")
	print()
	for key in pairs:
		print("key: ",key)
		print("value: ", pairs[key])
		print()
	print("------")

	# define nodes
	i=0
	j=0
	k=0
	pathList=[]
	for char in path:
		j+=1
		if char == '/':
			pathList.append(path[k:j-1])
			k=j
	pathList.append(path[k:])

	# parse tree
	try:
		tree = ET.parse(inputf)
		roots = []
		roots.append(tree.getroot())
		
		# loop through nodes and remove unwanted elements
		for i, node in enumerate(pathList):
			print("iteration: ", i+1, " node: ", node)
			newroots = []
			for root in roots:
				for child in list(root):
					if child.tag != node:
						addToRemovedList(child.tag)
						root.remove(child)
					else:
						if i == len(pathList) -1: # last node
							found = True
							for key, value in pairs.items():
								if not found:
									break
								found = False
								for c in child:
									if c.tag == key:
										if c.text == value:
											found = True
											break
							if not found:
								addToRemovedList(child.tag)
								root.remove(child)
							else: print("keep ", child.tag)
						else:
							print("keep ", child.tag) 
							newroots.append(child)
			roots = newroots
			print()
	
		# write to output
		if outputf != '':
			tree.write(outputf, encoding="UTF-8", xml_declaration=True)
			logSuccess(outputf, time.time())
		
			print()
			print("Removed:")
			for element, number in removedElements.items():
				print(element, " (", number, ")")
		else:
			return tree
	except OSError as e:
		print("-----File not found. See log file-----")
		logOSError(e, time.time())

def logOSError(e, timestamp):
	f = open('elementparser.log', 'a')
	log = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S') + " Error: " + e.strerror + " " + e.filename + "\n"
	f.write(log)
	f.close()

def logSuccess(filename, timestamp):
	f = open('elementparser.log', 'a')
	log = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S') + " Successful write: " + filename + "\n"
	f.write(log)
	f.close()

if __name__ == "__main__":
    main()