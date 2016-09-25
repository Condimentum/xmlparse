#!/usr/bin/python

import argparse
import valueparser
import os
import json
import dicttoxml

def main():
	parser = argparse.ArgumentParser(description='XML parser')
	parser.add_argument('inputdir', metavar='<Input File>', type=str, help='input file')
	parser.add_argument('keys', type=str, nargs='*', help='Define key values.')
	parser.add_argument('--path', type=str, help='Define path to root element where program starts searching for keys. Syntax: parent/child/grandchild. If not defined, document root used as root element.')
	parser.add_argument('--output', type=str, help='Output file')
	# parse args
	args = parser.parse_args()

	# default values
	outputf = None
	path = None
	
	# define search keys
	if args.keys is not None:
		keys = args.keys
	
	# define nodes
	if args.path is not None:
		path = "./" + args.path
	
	# define input file
	if args.inputdir is not None:
		inputdir = args.inputdir

	if args.output is not None:
		outputf, extension = os.path.splitext(args.output)

	print("inputdir:", inputdir)
	print("keys:", keys)

	dictList = []
	for filename in os.listdir(inputdir):
		dictList.extend(valueparser.parseValues(inputdir+"\\"+filename, keys, path=path))

	print(dictList)

	if outputf is not None:
		outputf=outputf+extension
		if extension.lower() == '.json':
			with open (outputf, 'w') as outfile:
				json.dump(dictList, outfile)
			print("Write to", outputf)
		elif extension.lower() == '.xml':
			f = open(outputf, 'w')
			f.write(dicttoxml.dicttoxml(dictList).decode("utf-8"))
			print("Write to", outputf)
		else:
			print("Extension for output file must be .json or .xml")

if __name__ == "__main__":
    main()