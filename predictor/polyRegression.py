import csv
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model

y = []
sum = 0
with open("day_count.csv", "rb") as inputfile:
	inputfile.readline()

	reader = csv.reader(inputfile, delimiter = ",")
	for row in reader:
		y.append(row[1])
		sum += int(row[1])

y = np.array(y).astype("int")

X = np.arange(1, len(y) + 1)

print(len(X))

z = np.polyfit(X, y, 2)

p = np.poly1d(z)

xp = np.linspace(1, len(X), 2*len(y))

_ = plt.plot(X, y, '.', xp, p(xp), '-')
# _ = plt.plot(X, y.astype("float")/sum, '.')

plt.show()