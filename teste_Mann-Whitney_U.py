import numpy as np
from scipy.stats import mannwhitneyu


# Introduction
# Welcome to lesson two on Hypothesis Testing with Python! Today's focus is on the Mann-Whitney U test. We've previously discussed T-tests, but now we're shifting attention to the Mann-Whitney U test, used to compare two independent samples. This tool helps when data doesn't meet the normality assumption for T-tests. In this lesson, we explore the ins and outs of the Mann-Whitney U test, applying it to a real-life dataset using Scipy.

# Mann-Whitney U Test Overview
# Let's start with non-parametric tests. These are also called distribution-free tests; they work with data that doesn't fit a normal distribution. We use them when our data is skewed, ordinal, or has outliers. Here, ordinal means a type of data where the order of the data points matters, but not the difference between the data points. For example, the sequence in which participants finish matters in a race, but the exact time difference between each runner does not.

# The Mann-Whitney U test compares two independent groups when the dependent variable is ordinal or continuous but doesn't follow a normal distribution. It ranks the values from the two groups and adds the ranks. Similar sums of ranks indicate the two groups are not significantly different.

# The Mann-Whitney U test provides two values: the U-statistic and the p-value. The U-statistic signifies the rank sum difference between two groups regarding their observed data values. In everyday language, the larger the U-statistic, the more separation or difference between the two groups' data. The p_value here means the same as in the T-test: If the p-value is less than 0.05, we conclude that the difference is statistically significant and not due to randomness.

# Performing the Test in Python
# The mannwhitneyu() function from Scipy runs the U test, taking two data samples as input and returning a test statistic (U) and a p-value (p). Here's what the code looks like:

# Define two distinct data samples
data1 = np.array([5, 22, 15, 18, 12, 17, 14])
data2 = np.array([25, 22, 30, 19, 23])

# Perform the Mann-Whitney U test
U, p = mannwhitneyu(data1, data2)

# Print the test statistic and p-value
print(f'U-value:\n {U}')  # 1.5
print(f'p-value:\n {p:.2f}')  # 0.0117

# If the p-value is less than 0.05, we consider it evidence against the null hypothesis, leading to its rejection.

# A Real-World Example
# Let's try the Mann-Whitney U test on some actual data. Suppose we have information about time spent on a website by users from two regions. The mission is to determine if there's a significant difference between these user types.

# Data on time spent (in minutes) on the website by users
time_A = np.array([31, 22, 39, 27, 35, 28, 34, 26, 23, 33])
time_B = np.array([26, 25, 30, 28, 29, 28, 27, 30, 27, 28])

# Perform the Mann-Whitney U test
U, p = mannwhitneyu(time_A, time_B)

# Print out the results
print(f'U-value:\n {U}')  # 60
print(f'p-value:\n {p:.2f}')  # 0.47

# The p-value is not below 0.05, it means there isn't a considerable difference.