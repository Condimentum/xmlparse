#!/urs/bin/python

import argparse

def main():
	# Alustetaan komentoriviparametrit
	parser = argparse.ArgumentParser(description='File name parser')
	parser.add_argument('--searchstring', metavar='Search String', type=str, help='String before file name')
	parser.add_argument('--startindex', metavar='Start index', type=int, help='Cut filename from beginning')
	parser.add_argument('--endindex', metavar='End index', type=int, help='Cut filename from end')
	parser.add_argument('--appendBefore', metavar='Append before', type=str, help='Append string before filename')
	parser.add_argument('--appendAfter', metavar='Append after', type=str, help='Append string after filename')
	parser.add_argument('inputf', metavar='<Input File>', type=str, help='input file')
	
	# Parsitaan komentoriviparametrit
	args = parser.parse_args()

	# Default values
	searchstring = ""
	startindex = 0
	endindex = None
	appendBefore = ""
	appendAfter = ""
	
	if args.searchstring is not None:
		searchstring = args.searchstring

	if args.startindex is not None:
		startindex = args.startindex

	if args.endindex is not None:
		endindex = args.endindex

	if args.appendBefore is not None:
		appendBefore = args.appendBefore

	if args.appendAfter is not None:
		appendAfter = args.appendAfter

	if args.inputf is not None:
		inputf = args.inputf

	# END OF Parsitaan komentoriviparametrit

	parsefilenames(inputf, searchstring, startindex, endindex, appendBefore, appendAfter)

def parsefilenames(inputf, searchstring="", startindex=0, endindex=None, appendBefore="", appendAfter=""):

	strln = len(searchstring)
	filenames = []
	
	# Luetaan tiedostoa rivi kerrallaan
	with open(inputf) as f:
		for line in f:
			index = line.find(searchstring) + startindex # Etsitään oikea kohta hakuehdon perusteella
			index = index + strln
			for i, char in enumerate(line[index:]): # välilyönnit pois alusta
				if not char.isspace():
					break
				index += 1
			if endindex is not None:
				lastindex = index + endindex
			else:
				lastindex = len(line)
				for i, char in enumerate(line[index:]):
					if char.isspace():
						lastindex = index + i 
						break
			#endindex -= 1
			filename = appendBefore + line[index:lastindex] + appendAfter
			print(filename)
			filenames.append(filename)

	print("remove duplicates:")
	filenames = list(set(filenames))
	filenames = list(filter(None, filenames)) # Poistetaan duplikaatit
	print(filenames)
	return filenames

if __name__ == "__main__":
    main()