#!/usr/local/bin/python

import json, argparse, sys
	

def readJson(filename):
	print "Read JSON from file: %s" % filename
	with open(filename, 'r') as inFileObj:
		jsonDict = json.load(inFileObj)
		
	return jsonDict	
		
def writeJson(inputDict, outFile):
	
	print "Writing JSON to file %s" % outFile
	
	with open(outFile, 'w') as outFileObj:
		# Flat
		#json.dump(inputDict, outFileObj)
		# Pretty Print
		#json.dump(inputDict, outFileObj, indent=2, separators=(',',': '))
		# Pretty Print - sorted
		json.dump(inputDict, outFileObj, indent=2, separators=(',',': '), sort_keys=True)
		
	print "Created JSON file %s" % outFile
	

if __name__ == "__main__":

	print "Starting JSON Printer"
	
	if len(sys.argv) > 1:
		print "Args: %s" % " ".join(sys.argv[1:])

	parser = argparse.ArgumentParser(description="JSON Printer")
	parser.add_argument("--action", dest="action", required=False, default="sort", choices=["convert", "sort"], help="Convert dict to JSON or sort JSON from input file")
	parser.add_argument("--outFile", dest="outputFileName", required=False, default="output.json", help="Name of file to write sorted JSON to")
	parser.add_argument("--inFile", dest="inputFileName", required=False, default="input.json", help="Name of input file containing JSON to sort")	
	args = parser.parse_args()
	
	if args.action == "convert":
		tempDict = {}
	elif args.action == "sort":
		tempDict = readJson(args.inputFileName)
		
	writeJson(tempDict, args.outputFileName)