import csv
import numpy as np
from matplotlib import pyplot as plt

from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C


def f(x):
    """The function to predict."""
    return x * np.sin(x)

counts = []
y = {}
sum = 0
with open("day_count.csv", "rb") as inputfile:
	inputfile.readline()
	reader = csv.reader(inputfile, delimiter = ",")
	for row in reader:
		y[row[0]] = int(row[1])
		sum += int(row[1])
		counts.append(int(row[1]))

x = np.arange(1, 366 + 1).reshape((366, 1))

counts = counts

# dy = 0.5 + 1.0 * np.random.random(len(counts))
# noise = np.random.normal(0, dy)
# counts += noise

# Instanciate a Gaussian Process model
kernel = C(1.0, (1e-3, 1e3)) * RBF(10, (1e-2, 1e2))
# kernel =  C(300000, (1e-5, 1e5))*RBF(10, (1e-3, 1e3))
gp = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=9)

gp.fit(x, counts)

xp = np.linspace(1, len(x), 2*len(x)).reshape((2*len(x), 1))

# Make the prediction on the meshed x-axis (ask for MSE as well)
y_pred, sigma = gp.predict(xp, return_std=True)

print gp.kernel_
print sigma

plt.plot(x, counts, '.')
plt.plot(xp, y_pred, 'b-', label=u'Prediction', color="green")
plt.fill(np.concatenate([xp, xp[::-1]]),
         np.concatenate([y_pred - 1.9600 * sigma,
                        (y_pred + 1.9600 * sigma)[::-1]]),
         alpha=.5, fc='b', ec='None', label='95% confidence interval')
plt.show()
