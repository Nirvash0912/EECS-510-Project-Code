import csv
import numpy as np
import time

# Convert datatime in tweet metadata files into timestamp

def readFiles(files):
	dates = []
	for file in files:
		with open(file, 'rb') as csvfile:
			reader = csv.reader(csvfile, delimiter=';')
			csvfile.readline()
			for row in reader:
				dates.append(row[1])
	return dates

if __name__ == '__main__':
	files = ['../output_got_part_1.csv', '../output_got_part_2.csv', '../output_got_part_3.csv']
	dates = readFiles(files)
	with open("timestamp.csv", "w") as output:
		output.write("timestamp\n")
		for date in dates:
			timestamp = int(time.mktime(time.strptime(date, '%Y-%m-%d %H:%M'))) - time.timezone
			output.write(str(timestamp) + "\n")