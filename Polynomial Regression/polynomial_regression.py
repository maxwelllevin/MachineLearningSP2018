"""
CS 369: AI and Machine Learning
Polynomial Regression Lab
March 23, 2018
Max, Will, Peter, Ben
"""

import numpy as np
import matplotlib.pyplot as plt


# ======== Generate Data ======== #

def build_function(degree):
	""" Builds a polynomial of given degree with coefficients uniformly distributed between -0.5 and 0.5. """
	coeffs = np.random.random(degree + 1) - 0.5
	return lambda x: sum([a * x ** i for i, a in enumerate(coeffs)])


def steve(numPoints):
	""" Generates random x values between -2 and 2. """
	return 4 * np.random.random(numPoints) - 2


# Add random noise (normally distributed with mean 0 and standard deviation 1) to each y value
def getYValsWithNoise(xVals, func):
	""" Generate y values given a set of x values and a function. Adds noise that is normally distributed with mean 0 and standard deviation 1. """
	return np.array([func(x) + np.random.normal() for x in xVals])


# Generate testing data without noise, using 100 'x' values uniformly distributed on the interval [-2, 2]
def getYVals(xVals, func):
	""" Generate y values given a set of x values and a function. """
	return np.array([func(x) for x in xVals])


# TODO: For testing purposes (not final product), plot training and testing data

test_data_1 = 0

f2 = build_function(2)
x1 = steve(100)
y1 = getYVals(x1, f2)

plt.scatter(x1, y1)

plt.xlim((-2, 2))
plt.show()

# ======== Fit Polynomials ======== #

# TODO: Use sklearn.linear_model.LinearRegression to fit polynomials of various degrees to the training data

# TODO: Be able to produce plots showing the training and testing data, true function, and several approximation functions

# TODO: Do this for 10, 100, and 1000 data points for polynomials of degrees 1, 2, and 20


# ======== Compare Polynomials ======== #

# TODO: Repeat the above experiment 100 times, using all of the model polynomial degrees 0 through 20.

# TODO: For 10, 100, and 1000 data points, produce a plot showing the average mean squared error (across all 100 runs) for the training and testing sets
