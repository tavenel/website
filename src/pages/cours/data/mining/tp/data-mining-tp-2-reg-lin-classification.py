# Load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read in the data
students = pd.read_csv('students-breakfast.csv')

# Create the scatter plot here:
plt.scatter(students.breakfast, students.score)

# Calculate group means
means = students.groupby('breakfast').mean().score
# ou :
#mean_score_no_breakfast = np.mean(students.score[students.breakfast == 0])
#mean_score_breakfast = np.mean(students.score[students.breakfast == 1])
print(means)

# Add the additional line here:
plt.plot(means, color='red')

# Show the plot
plt.show()



# Fit the model and print the coefficients
model = sm.OLS.from_formula('score ~ breakfast', students)
results = model.fit()
print(results.params)

# Calculate and print the difference in group means
print(mean_score_breakfast - mean_score_no_breakfast)
