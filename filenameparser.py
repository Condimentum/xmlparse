#!/urs/bin/python

import argparse

def main():
	parser = argparse.ArgumentParser(description='File name parser')
	parser.add_argument('--searchstring', metavar='Search String', type=str, help='String before file name')
	parser.add_argument('inputf', metavar='<Input File>', type=str, help='input file')
	
	args = parser.parse_args()
	
	if args.searchstring is not None:
		searchstring = args.searchstring

	if searchstring is None:
		searchstring = ''

	if args.inputf is not None:
		inputf = args.inputf

	parsefilenames(searchstring, inputf)

def parsefilenames(searchstring, inputf):

	strln = len(searchstring)
	filenames = []
	
	with open(inputf) as f:
		for line in f:
			index = line.find(searchstring)
			index = index + strln
			for i, char in enumerate(line[index:]): # välilyönnit pois alusta
				if char != ' ':
					break
				index += 1
			endindex = len(line)
			for i, char in enumerate(line[index:]):
				if char == ' ':
					endindex = index + i 
					break
			endindex -= 1
			print(line[index:endindex])
			filenames.append(line[index:endindex])

	print("remove duplicates:")
	filenames = list(set(filenames))
	filenames = list(filter(None, filenames))
	print(filenames)
	return filenames

if __name__ == "__main__":
    main()