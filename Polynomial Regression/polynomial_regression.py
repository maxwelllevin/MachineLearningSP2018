"""
CS 369: AI and Machine Learning
Polynomial Regression Lab
March 23, 2018
Max, Will, Peter, Ben
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression


def build_function(degree, coeffs=np.zeros((1, 1))):
	""" Builds a polynomial of given degree with random coefficients. """
	if not coeffs.any():
		coeffs = np.random.random(degree + 1) - 0.5
	return lambda x: sum([a * x ** i for i, a in enumerate(coeffs)])


def steve(numPoints):
	""" Generates random x values between -2 and 2. """
	return 4 * np.random.random((numPoints, 1)) - 2


def getYValsWithNoise(xVals, func):
	""" Generate y values given a set of x values and a function. Adds noise that is normally distributed with mean 0 and standard deviation 1. """
	return np.array([func(x) + np.random.normal() for x in xVals])


def getYVals(xVals, func):
	""" Generate y values given a set of x values and a function. """
	return np.array([func(x) for x in xVals])


def meanSquareError(func_a, func_b, x_vals):
	""" returns the mean squared error of two functions with a shared np.array of x values """
	summation = 0
	for x in x_vals:
		summation += (func_a(x) - func_b(x)) ** 2
	return summation / x_vals.size


# ======== Generate Testing Data ======== #

# Random Polynomial functions used to generate data
f1, f2, f20 = build_function(1), build_function(2), build_function(20)

# Test data for 10 points
x_test_10 = steve(10)
y_test_d1_10, y_test_d2_10, y_test_d20_10 = getYVals(x_test_10, f1), getYVals(x_test_10, f2), getYVals(x_test_10, f20)

# Test data for 100 points
x_test_100 = steve(100)
y_test_d1_100, y_test_d2_100, y_test_d20_100 = getYVals(x_test_100, f1), getYVals(x_test_100, f2), getYVals(x_test_100,
                                                                                                            f20)

# Test data for 1000 points
x_test_1000 = steve(1000)
y_test_d1_1000, y_test_d2_1000, y_test_d20_1000 = getYVals(x_test_1000, f1), getYVals(x_test_1000, f2), getYVals(
		x_test_1000, f20)

# ======== Generate Training Data ======== #

# Training data for 10 points
x_train_10 = steve(10)
y_train_d1_10, y_train_d2_10, y_train_d20_10 = getYValsWithNoise(x_train_10, f1), getYValsWithNoise(x_train_10,
                                                                                                    f2), getYValsWithNoise(
		x_train_10, f20)

# Training data for 100 points
x_train_100 = steve(100)
y_train_d1_100, y_train_d2_100, y_train_d20_100 = getYValsWithNoise(x_train_100, f1), getYValsWithNoise(x_train_100,
                                                                                                        f2), getYValsWithNoise(
		x_train_100,
		f20)

# Training data for 1000 points
x_train_1000 = steve(1000)
y_train_d1_1000, y_train_d2_1000, y_train_d20_1000 = getYValsWithNoise(x_train_1000, f1), getYValsWithNoise(
		x_train_1000, f2), getYValsWithNoise(
		x_train_1000, f20)

# ======== Plot Stuff ======== #
f2 = build_function(3)
x1 = steve(100)
y1 = getYValsWithNoise(x1, f2)

poly_features = PolynomialFeatures(degree=3, include_bias=False)
X_poly = poly_features.fit_transform(x1)
lin_reg = LinearRegression()
lin_reg.fit(X_poly, y1)

coefficients = np.insert(lin_reg.coef_, 0, lin_reg.intercept_)

x_values = np.arange(-2, 2, .001)
guess_y = getYVals(x_values, build_function(2, coefficients))
real_y = getYVals(x_values, f2)

plt.plot(x_values, real_y, color="green", linewidth=3)
plt.plot(x_values, guess_y, color="orange", linewidth=3)
plt.scatter(x1, y1)

plt.xlim((-2, 2))
# plt.ylim((-10,10))
plt.show()

print(meanSquareError(f2, build_function(2, coefficients), x_values))

# ======== PROJECT REQUIREMENTS ======== #

# TODO: A single run showing 10 training points, true test curve, and fit polynomials of 1, 2, and 20 degrees

# TODO: Ditto but for 100 training points

# TODO: Ditto but for 1000 training points

# TODO: Training and testing mean squared error, averaged over 100 runs with 10 training points each, as a function of model degree 0 through 20

# TODO: Ditto but for 100 training points

# TODO: Ditto but for 1000 training points
