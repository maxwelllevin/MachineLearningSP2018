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


def mse(data1, data2):
	if len(data1) != len(data2):
		print("ERROR: Data arrays are not of the same length! ")
		print("ERROR: Data array 1 is of length ", len(data1), " while data array 2 is of length ", len(data2), ".")
		exit(-1)
	error = 0
	for a, b in zip(data1, data2):
		error += (a - b) ** 2
	return error / len(data1)


def avg_mse(num_points, num_runs=100, num_degrees=20, f_degree=4):
	""" Computes and plots MSE for training and testing data averaged over 100 runs for fit polynomials of degree 0 through 20. """
	train_mse = [0] * (num_degrees + 1)
	test_mse = [0] * (num_degrees + 1)
	for run in range(num_runs):
		func = build_function(f_degree)

		# Gen training and testing data
		train_x = gen_x_values(num_points)
		train_y = gen_training_data(train_x, func)
		test_x = np.linspace(-2, 2, num_points)
		test_y = gen_testing_data(test_x, func)

		# Fit the polynomial for each degree
		for deg in range(1, 21):
			fit_deg = fit_polynomial(train_x, train_y, deg)  # Fit the polynomial from the training data
			train_fit_y = gen_testing_data(train_x, fit_deg)  # Get the fit polynomial values for the training x values
			test_fit_y = gen_testing_data(test_x, fit_deg)  # Same but for the testing x values
			train_mse[deg] += mse(train_y, train_fit_y) / num_runs
			test_mse[deg] += mse(test_y, test_fit_y) / num_runs

		# Fit the polynomial for degree 0
		fit_deg = sum(train_y) / len(train_y)
		train_mse[0] = mse(train_y, [fit_deg] * len(train_y))
		test_mse[0] = mse(test_y, [fit_deg] * len(test_y))

	plt.plot(range(21), train_mse, label="Training Set")
	plt.plot(range(21), test_mse, color="orange", label="Validation Set")
	plt.title("Mean Squared Error for " + str(num_points) + " Data Points")
	plt.xlabel("Degrees")
	plt.xticks(np.arange(0, 21, step=1))
	plt.ylabel("Mean Squared Error")
	plt.ylim(0, test_mse[0])
	plt.legend()
	plt.show()


single_run(10)
single_run(100)
single_run(1000)
avg_mse(10)
avg_mse(100)
avg_mse(1000)
