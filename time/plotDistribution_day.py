import csv
import matplotlib.pyplot as plt
import numpy as np

# plot distribution of tweets based on day

if __name__ == '__main__':
	date = []
	count = []
	with open("day_count.csv", 'rb') as csvfile:
		csvfile.readline()
		reader = csv.reader(csvfile, delimiter=',')
		csvfile.readline()
		for row in reader:
			date.append(row[0])
			count.append(row[1])

	x = range(len(date))
	plt.plot(x, count)
	plt.xticks(range(len(date)), date)
	plt.show()