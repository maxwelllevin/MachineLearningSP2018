"""
Algorithm to visualize the k-means clustering algorithm
"""
import random

import matplotlib.pyplot as plt
import numpy as np


def make_cluster(u, v, npts=1000, sd=0.25):
	""" Returns an array of normally distributed points with center (u,v). """
	return sd * np.random.randn(npts, 2) + (u, v)


def make_many_clusters(nclust=3, low=0, high=10):
	""" Returns a list of points from many clusters with random centers."""
	clusters = []
	for i in range(nclust):
		x_pos, y_pos = random.randint(low, high + 1), random.randint(low, high + 1)
		clusters += list(make_cluster(x_pos, y_pos, random.randint(100, 600)))
	return np.array(clusters)


def pick_initial_centroid(data, k=3):
	""" Returns a list of k random (x,y) pairs from data. """
	return np.array(random.choices(data, k=k))


# TODO: Define a distance function

# TODO: Define function to mark all points to closest centroid

# TODO: Update Centroid location


# ================= Test our functions =================#
# Get the data & plot it
pts = make_many_clusters()
plt.scatter(pts[:, 0], pts[:, 1], s=0.8, c="xkcd:sky blue")

# Pick Centroids and plot them
centroids = pick_initial_centroid(pts)
plt.scatter(centroids[:, 0], centroids[:, 1], s=20, c="xkcd:salmon", marker="^")

plt.axes().set_aspect('equal', 'datalim')
plt.show()
