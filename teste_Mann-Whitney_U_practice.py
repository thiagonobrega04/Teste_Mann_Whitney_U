import numpy as np
from scipy.stats import mannwhitneyu

# Can web analytics tell us whether visitors from City X and City Y spend different amounts of time on a website? The given code performs the Mann-Whitney U test to find out. Click Run to see the analysis in action!

# Sample data representing time spent on a website from two different cities
city_x = np.array([12, 15, 14, 18, 13])
city_y = np.array([20, 22, 24, 19, 21])

# Perform the Mann-Whitney U test
statistic, p_value = mannwhitneyu(city_x, city_y)
print(f'Mann-Whitney U statistic: {statistic:.2f} \n P-value: {p_value:.2f}')

# Now for a bit of coding magic! Let's enhance the output from the Mann-Whitney U test you just ran. Add a conditional message to communicate the statistical significance based on the p-value. Print out either "Reject the null hypothesis, there is a significant difference." or "Fail to reject the null hypothesis, there is not a significant difference." based on the p-value. Use 0.05 as a threshold.

# Ready to spellbind the data? Let's code!

# Page visits by two different referer sources
referer1 = [42, 35, 28, 50, 41]
referer2 = [34, 32, 23, 39, 29]

# Perform the Mann-Whitney U test
test_statistic, p_value = mannwhitneyu(referer1, referer2)

# Output the results for interpretation
print(f'Test Statistic: {test_statistic:.2f}\n p-value: {p_value:.2f}')

significance_level = 0.05
if p_value < significance_level:
    print("Reject the null hypothesis, there is a significant difference.")
else:
    print("Fail to reject the null hypothesis, there is not a significant difference.")

# Great orbiting, Space Voyager! Now harness the power of the stars to fill in the blank: perform the Mann-Whitney U test on our web layout samples and output their U-value and p-value. Don't forget to also make a conclusion: print out whether we reject the null hypothesis or not!

# Web analytics: average time on page for two different design layouts
layout_A_time = np.array([120, 115, 130, 140, 125])
layout_B_time = np.array([110, 108, 123, 135, 118])

# TODO: Perform the Mann-Whitney U test on the two sets of layout times.
U_value, p_value = mannwhitneyu(layout_A_time, layout_B_time)

# Output the U-value and p-value with two decimal places for U-value and four for p-value.
print(f'U_value: {U_value:.2f}\n p_value: {p_value:.4f}')

# TODO: Make a conclusion
significance_level = 0.05
if p_value < significance_level:
    print("Reject the null hypothesis, there is a significant difference.")
else:
    print("Fail to reject the null hypothesis, there is not a significant difference.")

# Fantastic progress, Space Voyager! In order to demonstrate the Mann-Whitney U test behaviour, your new mission is to adjust the second array sample_B in the code to have statistical difference from the first array sample_A.

# The acceptance criteria for this task is that obtained p_value should be lower than 0.05, but greater than 0.001.

# Define two data samples for comparison
sample_A = [50, 45, 40, 55, 60]
sample_B = [40, 30, 35, 40, 35]  # Re-assign values

# Let's see how these two sample groups compare using the Mann-Whitney U test
U_stat, p_value = mannwhitneyu(sample_A, sample_B)
print(f'U-statistic: {U_stat:.4f}\n p-value: {p_value:.4f}')