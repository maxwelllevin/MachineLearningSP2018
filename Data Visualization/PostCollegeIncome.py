import pandas as pd
import matplotlib.pyplot as plt

# Read in the file
dpb_file = pd.read_csv('degrees-that-pay-back.csv')
# sbc_file = pd.read_csv('salaries-by-college-type.csv')


# Grab the degrees
degrees = dpb_file.get('Undergraduate Major')
degrees = [d for d in degrees]

# Grab the Salaries - Starting Median, Mid-Career Median, 10th, 25th, 75th, 90th Percentile Mid-Career Salaries
start_sal_50 = dpb_file.get('Starting Median Salary')
mid_sal_10 = dpb_file.get('Mid-Career 10th Percentile Salary')
mid_sal_25 = dpb_file.get('Mid-Career 25th Percentile Salary')
mid_sal_50 = dpb_file.get('Mid-Career Median Salary')
mid_sal_75 = dpb_file.get('Mid-Career 75th Percentile Salary')
mid_sal_90 = dpb_file.get('Mid-Career 90th Percentile Salary')

# Clean the salary data (strip the $'s and ,'s  from the strings, and convert to numbers
salary_data = [start_sal_50, mid_sal_10, mid_sal_25, mid_sal_50, mid_sal_75, mid_sal_90]
for i in range(len(salary_data)):
	salary_data[i] = salary_data[i].map(lambda x: x.replace("$", ""))
	salary_data[i] = salary_data[i].map(lambda x: x.replace(",", ""))
	salary_data[i] = salary_data[i].map(lambda x: float(x))
start_sal_50, mid_sal_10, mid_sal_25, mid_sal_50, mid_sal_75, mid_sal_90 = salary_data


# TODO: Plot Salaries vs Degrees
fig = plt.figure()
plt.scatter(start_sal_50, degrees)
plt.show()