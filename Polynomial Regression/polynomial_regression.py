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

plt.rcParams["font.family"] = "Times New Roman"


def build_function(degree, coeffs=np.zeros((1, 1))):
	""" Builds a polynomial of given degree with random coefficients. """
	if not coeffs.any():
		coeffs = np.random.random(degree + 1) - 0.5
	return lambda x: sum([a * x ** i for i, a in enumerate(coeffs)])


def gen_x_values(num_pts):
	""" Generates random x values between -2 and 2. """
	return 4 * np.random.random((num_pts, 1)) - 2


def gen_training_data(x_vals, func):
	""" Generate y values given a set of x values and a function. Adds noise that is normally distributed with mean 0 and standard deviation 1. """
	return np.array([func(x) + np.random.normal() for x in x_vals])


def gen_testing_data(x_vals, func):
	""" Generate y values given a set of x values and a function. """
	return np.array([func(x) for x in x_vals])


def mean_squared_error(func_a, func_b, x_vals):
	""" returns the mean squared error of two functions with a shared np.array of x values """
	summation = 0
	for x in x_vals:
		summation += (func_a(x) - func_b(x))**2
	return summation / x_vals.size


def fit_polynomial(training_x, training_y, deg):
	""" Send training data and the degree you would like to fit to. Returns a function. """
	if deg == 0:
		return lambda x: sum(training_y) / len(training_y)
	poly_features = PolynomialFeatures(degree=deg, include_bias=False)
	X_poly = poly_features.fit_transform(training_x)
	lin_reg = LinearRegression()
	lin_reg.fit(X_poly, training_y)
	coefficients = np.insert(lin_reg.coef_, 0, lin_reg.intercept_)
	return build_function(2, coefficients)


def single_run(num_points):
	f4 = build_function(4)
	x1 = gen_x_values(num_points)
	y1 = gen_training_data(x1, f4)

	x_values = np.arange(-2, 2, .001)
	guess_y_d1 = gen_testing_data(x_values, fit_polynomial(x1, y1, 1))
	guess_y_d2 = gen_testing_data(x_values, fit_polynomial(x1, y1, 2))
	guess_y_d20 = gen_testing_data(x_values, fit_polynomial(x1, y1, 20))
	real_y = gen_testing_data(x_values, f4)

	plt.plot(x_values, real_y, color="green", linewidth=1, label="Actual")
	plt.plot(x_values, guess_y_d1, color="orange", linewidth=1, label="Fit 1 Degree")
	plt.plot(x_values, guess_y_d2, color="blue", linewidth=1, label="Fit 2 Degrees")
	plt.plot(x_values, guess_y_d20, color="red", linewidth=1, label="Fit 20 Degrees")
	plt.scatter(x1, y1, s=2, label="Training Data")

	plt.xlim((-2, 2))
	plt.ylim((-10, 10))
	plt.legend()
	plt.title("Polynomial Fitting for " + str(num_points) + " Data Points")
	plt.show()


def average_error_run(num_points):
	mean_squared_errors = []
	sum_mean_squared_errors = [0] * 21

	for run in range(100):
		f4 = build_function(4)
		x1 = gen_x_values(num_points)
		y1 = gen_training_data(x1, f4)
		x_values = np.arange(-2, 2, 0.001)

		for degree in range(21):
			sum_mean_squared_errors[degree] += mean_squared_error(f4, fit_polynomial(x1, y1, degree), x_values) / 100

	plt.plot(range(21), sum_mean_squared_errors)
	plt.title("Mean Squared Error for " + str(num_points) + " Data Points")
	plt.xlabel("Degrees")
	plt.xticks(np.arange(0, 21, step=1))
	plt.ylabel("Mean Squared Error")
	plt.show()


single_run(10)
single_run(100)
single_run(1000)
average_error_run(10)
average_error_run(100)
average_error_run(1000)
