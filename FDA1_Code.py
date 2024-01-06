#Imports

import pandas as pd
import numpy as np 
import os
import matplotlib.pyplot as plt

# Loading the Iris Data Set
IrisData = pd.read_csv('Iris.csv')
IrisData.head()

# Dropping unwanted columns
IrisData= IrisData.drop(columns= ['Id'])
IrisData.head()

# Print info on data frame
IrisData.info()

# Identify null values
IrisData.isnull().sum()

# Plotting Histogram of sepal width for all irises
x = np.array(IrisData['SepalWidthCm'])
plt.title("Sepal Width for All Irises", loc = 'center')
plt.xlabel("Sepal Width Cm")
plt.ylabel("No. Irises")

plt.hist(x, color= 'orange', edgecolor='purple')
plt.show()
