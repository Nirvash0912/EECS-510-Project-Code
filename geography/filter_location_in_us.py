import os
import csv
import json

# Filter out the tweets with US locations

outputfile_prefix = "location_in_us"

def readStates():
	states = {}
	with open("./states.csv", 'rb') as statesfile:
		reader = csv.reader(statesfile, delimiter=';')
		for row in reader:
			states[row[1]] = row[0]
	return states

def main():
	states = readStates()
	names = states.keys()
	

	i = 0
	for filename in os.listdir("./carmen_result"):
		if filename.endswith(".json"): 
			inputfilename = "./carmen_result/" + filename
			outputfilename = "./location_in_us/" + outputfile_prefix + str(i) +".json"
			with open(inputfilename, 'rb') as inputfile, open(outputfilename, 'a') as outputfile:
				for line in inputfile:
					temp = json.loads(line)
					location = temp[u'location']
					if location in names:
						outputfile.write(line)
		i += 1
			
main()


