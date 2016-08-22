#!/usr/bin/python

import elementparser
import filenameparser
import argparse

def main():
	# Komentoriviparametrien alustus
	parser = argparse.ArgumentParser(description='Main module')
	parser.add_argument('inputf', metavar='<Input File', type=str, help='Input File')
	parser.add_argument('outputf', type=str, help='Output File')
	parser.add_argument('pairs', type=str, nargs='*', help='key-value pairs')
	parser.add_argument('--xpath', type=str, help='Define path to root element')
	parser.add_argument('--filepath', type=str, help='Oikea tiedostopolku')
	parser.add_argument('--search', type=str, help='Search String')

	# Komentoriviparametrien parsiminen
	args=parser.parse_args()

	if args.inputf is not None:
		inputf = args.inputf

	if args.outputf is not None:
		outputf = args.outputf

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

	if args.search is not None:
		search = args.search

	if args.xpath is not None:
		path = args.xpath

	if args.filepath is not None:
		filepath = args.filepath

	# END OF Komentoriviparametrien parsiminen

	# Parsitaan tiedostonimet
	filenames = filenameparser.parsefilenames(inputf, searchstring=search, startindex=41, appendBefore=filepath)
	
	for i, filename in enumerate(filenames):
		print(filename)
		outputfilename = outputf + str(i) + ".xml"
		# Parsitaan elementit
		elementparser.parseElements(filename, pairs, path, outputfilename)
		# TODO: merkitään tiedosto luetuksi tai siirretään toiseen kansioon

if __name__ == "__main__":
	main()