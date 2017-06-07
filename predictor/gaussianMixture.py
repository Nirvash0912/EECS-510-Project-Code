from matplotlib import pyplot as plt
import numpy as np
from sklearn.mixture import GaussianMixture
import matplotlib.mlab as mlab
import csv

y = {}
counts = []
sum = 0
with open("day_count.csv", "rb") as inputfile:
	inputfile.readline()
	reader = csv.reader(inputfile, delimiter = ",")
	for row in reader:
		y[row[0]] = int(row[1])
		sum += int(row[1])
		counts.append(row[1])

counts = np.array(counts).astype("int")
samples = []
i = 1
for key, value in y.iteritems():
	for j in range(value):
		samples.append(i)
	i += 1

X = np.array(samples).reshape((len(samples), 1))

# y = np.array(y).astype("int").reshape((366, 1))

x = np.arange(1, 366 + 1)

# Fit a Gaussian mixture with EM using five components
gmm = GaussianMixture(n_components=2, covariance_type='full').fit(X)

# xp = np.linspace(1, len(X), 2*len(y))

print gmm.weights_
print gmm.means_
print gmm.covariances_

# x = np.linspace(1, len(y) + 1, 1000)
# plt.hist(samples, 366, histtype='stepfilled', alpha=0.4)
# print mlab.normpdf(x, gmm.means_[0][0], gmm.covariances_[0][0])
plt.plot(x, gmm.weights_[0] * mlab.normpdf(x, gmm.means_[0][0], np.sqrt(gmm.covariances_[0][0])) + gmm.weights_[1] *  mlab.normpdf(x, gmm.means_[1][0], np.sqrt(gmm.covariances_[1][0])), color ="green")
plt.plot(x, counts.astype("float")/sum, '.')
plt.show()