import csv
import matplotlib.pyplot as plt
import numpy as np

# Count the tweets in every month then plot the distribution

def readFiles(files):
	dates = []
	for file in files:
		with open(file, 'rb') as csvfile:
			reader = csv.reader(csvfile, delimiter=';')
			csvfile.readline()
			for row in reader:
				dates.append(row[1])
	return dates

def getYearMonth(dates):
	yearMonth = []
	for date in dates:
		tempTuple = []
		tempDate = date.split(' ')[0].split('-');
		tempTuple.append(tempDate[0])
		tempTuple.append(tempDate[1])
		yearMonth.append(tempTuple)
	return yearMonth

def getYearMonthDay(dates):
	ymd = []
	for date in dates:
		tempTriple = []
		tempDate = date.split(' ')[0].split('-');
		tempTriple.append(tempDate[0])
		tempTriple.append(tempDate[1])
		tempTriple.append(tempDate[2])
		ymd.append(tempTriple)

def tweetCount(yearMonth):
	dateCounts = {}
	for date in yearMonth:
		timeStamp = date[0] + '-' + date[1]
		if timeStamp in dateCounts:
			dateCounts[timeStamp] += 1
		else:
			dateCounts[timeStamp] = 1

	return dateCounts

if __name__ == '__main__':
	files = ['../output_got_part_1.csv', '../output_got_part_2.csv', '../output_got_part_3.csv']
	dates = readFiles(files)
	
	yearMonth = getYearMonth(dates)

	x = []
	y = []
	dateCounts = tweetCount(yearMonth)

	for key in sorted(dateCounts.iterkeys()):
		x.append(key)
		y.append(dateCounts[key])

	x = x[1:]
	y = y[1:]
	y_pos = np.arange(len(x))

 	with open("month_count.csv", "w") as out:
		out.write("date,value\n")
		for i in range(len(x)):
			out.write(x[i] + "," + str(y[i]) + "\n")

	plt.bar(y_pos, y, align='center', alpha=0.5)
	plt.xticks(y_pos, x)
	plt.ylabel('Count')
	plt.title('Distribution of tweets')

	plt.show()
	# fig = plt.figure()
	# fig.plot(dates, counts)