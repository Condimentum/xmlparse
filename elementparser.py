#!/urs/bin/python

import argparse
import xml.etree.ElementTree as ET
import xml.dom.minidom as DOM

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
	parser.add_argument('--path', type=str, help='Define path to root element where program starts searching for child elements. Syntax: parent/child/grandchild. If not defined, document root used as root element.')
	parser.add_argument('--output', type=str, help='Output file')
	
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
	
	print("---Search parameters---")
	print()
	for key in pairs:
		print("key: ",key)
		print("value: ", pairs[key])
		print()
	print("------")
	
	# define nodes
	if args.path is not None:
		i=0
		j=0
		k=0
		path=[]
		for char in args.path:
			j+=1
			if char == '/':
				path.append(args.path[k:j-1])
				k=j
		path.append(args.path[k:])
	
	# parse tree from xml
	tree = ET.parse(args.inputf)
	roots = []
	roots.append(tree.getroot())
	
	# loop through nodes and remove unwanted elements
	for i, node in enumerate(path):
		print("iteration: ", i+1, " node: ", node)
		newroots = []
		for root in roots:
			for child in list(root):
				if child.tag != node:
					addToRemovedList(child.tag)
					root.remove(child)
				else:
					if i == len(path) -1: # last node
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
	if args.output is None:
		args.output = 'output.xml'
	tree.write(args.output, encoding="UTF-8", xml_declaration=True)
	
	print()
	print("Removed:")
	for element, number in removedElements.items():
		print(element, " (", number, ")")

if __name__ == "__main__":
    main()