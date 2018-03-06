import csv
import matplotlib.pyplot as plt
import numpy as np


degree_filename = 'degrees-that-pay-back.csv'

with open(degree_filename, 'r') as degree_file:
	data_iter = csv.reader(degree_file)
	data = [data for data in data_iter]

headers = data[0]
data = data[1:]

# String list containing majors
majors = [d[0] for d in data]

# Salaries range from ~30k to 120k
start_mean_salary = [d[1] for d in data]
mid_mean_salary = [d[2] for d in data]

# Percentage increase from start to median salary
growth = [d[3] for d in data]

print(majors)