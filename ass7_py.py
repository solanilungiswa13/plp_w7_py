#Task 1
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Load the iris dataset
data = pd.read_csv('iris.csv')

print(data.head())

print(data.info())
print(data.isnull().sum()) #Check for missing values

#clean the dataset if needed
#data['sepal_length'].fillna(data['sepal_length'].mean(), inplace=True)
#data.dropna(inplace=True) # Uncomment if there are missing values

#Task 2
print(data.describe()) #Get basic statistics of the dataset

grouped = data.groupby('species')['sepal_length'].mean()
print(grouped)

#Task 3
# Line chart (if you have time-series data, replace 'species' with your time column)
# data.groupby('species')['sepal_length'].mean().plot(kind='line')
# plt.title('Mean Sepal Length by Species')
# plt.xlabel('Species')
# plt.ylabel('Mean Sepal Length')
# plt.show()

# Bar chart
grouped.plot(kind='bar')
plt.title('Mean Sepal Length by Species')
plt.xlabel('Species')
plt.ylabel('Mean Sepal Length')
plt.show()

# Histogram
plt.hist(data['sepal_length'], bins=10)
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
plt.show()

# Scatter plot
plt.scatter(data['sepal_length'], data['sepal_width'])
plt.title('Sepal Length vs. Sepal Width')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.show()