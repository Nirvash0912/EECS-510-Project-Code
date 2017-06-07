import os
import csv
import json
import datetime
from dateutil import parser

# Count the number of tweest based on state, results are overall distribution and monthly distributions

def readStates():
	states = {}
	with open("./states.csv", 'rb') as statesfile:
		reader = csv.reader(statesfile, delimiter=';')
		for row in reader:
			states[row[1]] = row[0]
	return states

def main():
	states = readStates()
	states_count = {}
	states_count_month = []

	for state in states.keys():
		states_count[state] = 0

	for i in range(12):
		temp_month = {}
		for state in states.keys():
			temp_month[state] = 0
		states_count_month.append(temp_month)

	for filename in os.listdir("./location_in_us"):
		if filename.endswith(".json"): 
			inputfilename = "./location_in_us/" + filename
			with open(inputfilename, 'rb') as inputfile:
				for line in inputfile:
					temp = json.loads(line)
					location = temp[u'location']
					time = temp[u'timestamp']
					time = parser.parse(time)
					
					states_count_month[time.month-1][location] += 1

					states_count[location] += 1
	
	with open("./location_stat/location_stat_overall.csv", 'w') as overall:
		overall.write("state,count\n")
		for loc, count in states_count.items():
			line = states[loc] + "," + str(count) + "\n"
			overall.write(line)


	i = 1
	for month_count in states_count_month:
		with open("./location_stat/location_stat_months" + str(i) + ".csv", 'w') as outputfile:
			outputfile.write("state,count\n")
			for loc, count in month_count.items():
				line = states[loc] + "," + str(count) + "\n"
				outputfile.write(line)
		i += 1

main()