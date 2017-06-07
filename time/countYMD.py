import csv
import matplotlib.pyplot as plt
import numpy as np

# Count the number of tweets at each day

def readFiles(files):
	dates = []
	for file in files:
		with open(file, 'rb') as csvfile:
			reader = csv.reader(csvfile, delimiter=';')
			csvfile.readline()
			for row in reader:
				dates.append(row[1])
	return dates

def getYearMonthDay(dates):
	ymd = []
	for date in dates:
		tempTriple = []
		tempDate = date.split(' ')[0].split('-');
		tempTriple.append(tempDate[0])
		tempTriple.append(tempDate[1])
		tempTriple.append(tempDate[2])
		ymd.append(tempTriple)
	return ymd

def tweetCount(yearMonth):
	dateCounts = {}
	for date in yearMonth:
		timeStamp = date[0] + '-' + date[1] + '-' + date[2]
		if timeStamp in dateCounts:
			dateCounts[timeStamp] += 1
		else:
			dateCounts[timeStamp] = 1

	return dateCounts

if __name__ == '__main__':
	files = ['../output_got_part_1.csv', '../output_got_part_2.csv', '../output_got_part_3.csv']
	dates = readFiles(files)
	
	yearMonth = getYearMonthDay(dates)

	x = []
	y = []
	dateCounts = tweetCount(yearMonth)

	for key in sorted(dateCounts.iterkeys()):
		x.append(key)
		y.append(dateCounts[key])

	x = x[1:]
	y = y[1:]
	y_pos = np.arange(len(x))

 	with open("day_count.csv", "w") as out:
		out.write("date,value\n")
		for i in range(len(x)):
			out.write(x[i] + "," + str(y[i]) + "\n")