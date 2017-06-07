import os
import csv
import json
import datetime
import matplotlib.pyplot as plt
from dateutil import parser
from matplotlib.font_manager import FontProperties

# Plot count change in each state based on month

def readStates():
	states = {}
	with open("./states.csv", 'rb') as statesfile:
		reader = csv.reader(statesfile, delimiter=';')
		for row in reader:
			states[row[1]] = row[0]
	return states

def main():
	states = readStates().values()
	state_counts = {}
	with open("./state_year.csv", 'rb') as statesfile:
		statesfile.readline()
		reader = csv.reader(statesfile, delimiter=',')
		for row in reader:
			state_counts[row[0]] = []
			for i in range(1, 13):
				state_counts[row[0]].append(row[i])
	x = range(1, 13)

	lines = []
	for state, month_count in state_counts.iteritems():
		line, = plt.plot(x, month_count, label=state)
		lines.append(line)

	plt.axis([1, 12, 0, 600])
	plt.xticks(x)
	plt.grid()
	# fontP = FontProperties()
	# fontP.set_size('small')
	# legend = plt.legend(handles=lines, prop=fontP)
	plt.show()
main()