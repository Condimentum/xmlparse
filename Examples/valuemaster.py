#!/usr/bin/python

import valueparser
import os
import json

def main():
	parser = argparse.ArgumentParser(description='XML parser')
	parser.add_argument('inputdir', metavar='<Input File>', type=str, help='input file')
	parser.add_argument('keys', type=str, nargs='*', help='Define key values.')
	parser.add_argument('--path', type=str, help='Define path to root element where program starts searching for keys. Syntax: parent/child/grandchild. If not defined, document root used as root element.')
	parser.add_argument('--output', type=str, help='Output file')
	# parse args
	args = parser.parse_args()
	
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
		outputf = args.output + ".json"

	dictList = []
	for filename in os.listdir(inputdir):
		dictList.extend(valueparser.parseValues(filename, keys, path, ''))

	if outputf is not None:
		with open (outputf, 'w') as outfile:
			json.dump(dictList, outfile)
		print("Write to", outputf)