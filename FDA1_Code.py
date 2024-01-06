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

# Histogram of sepal length for all irises
x = np.array(IrisData['SepalLengthCm'])
plt.title("Sepal Length for All Irises", loc = 'center')
plt.xlabel("Sepal Length Cm")
plt.ylabel("No. Irises")

plt.hist(x, color= 'red', edgecolor='blue')
plt.show()
# Histoogram of petal length for all irises
x = np.array(IrisData['PetalLengthCm'])
plt.title("Petal Length for All Irises", loc = 'center')
plt.xlabel("Petal Length Cm")
plt.ylabel("No. Irises")

plt.hist(x, color= 'blue', edgecolor='violet')
plt.show()

# Histoogram of petal Width for all irises
x = np.array(IrisData['PetalWidthCm'])
plt.title("Petal Width for All Irises", loc = 'center')
plt.xlabel("Petal Width Cm")
plt.ylabel("No. Irises")

plt.hist(x, color= 'gold', edgecolor='silver')
plt.show()

# Dual histogram to show sepal length and width for all irises
series1 = np.array(IrisData['SepalLengthCm'])
series2 = np.array(IrisData['SepalWidthCm'])
 
plt.hist(series1, label='Sepal Length', color= 'red', edgecolor='blue')
 
plt.hist(series2, label='Sepal Width', color = 'orange', edgecolor='purple')

plt.xlabel('Measurements in Cm')
plt.ylabel('No. Irises')
plt.title('All Irises Sepal Length & Sepal Width')
plt.legend()
plt.show()

# Scatterplot to show distribution and hexabin to show occurances for sepal dimensions for all irises
x = np.array(IrisData['SepalLengthCm'])
y = np.array(IrisData['SepalWidthCm'])

plt.hexbin(x, y, gridsize=30, cmap='Blues')
 
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('Most Common Sepal Width & Length All Irises')
plt.colorbar()
plt.show()

# Dual histogram to show petal length and petal for all irises
series1 = np.array(IrisData['PetalLengthCm'])
series2 = np.array(IrisData['PetalWidthCm'])
 
plt.hist(series1, label='Petal Length', color='blue', edgecolor='violet')
 
plt.hist(series2, label='Petal Width', color='gold', edgecolor='silver')

plt.xlabel('Measurements in Cm')
plt.ylabel('No. Irises')
plt.title('All Irises Petal Length & Petal Width')
plt.legend()
plt.show()

# Scatterplot to show distribution and hexabin to show occurances for petal dimensions for all irises
x = np.array(IrisData['PetalLengthCm'])
y = np.array(IrisData['PetalWidthCm'])

plt.hexbin(x, y, gridsize=30, cmap='Blues')
 
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.title('Most Common Petal Width & Length All Irises')
plt.colorbar()
plt.show()

# Read Iris setosa csv 
IrisSetosa = pd.read_csv('Iris_setosa.csv')
IrisData.head()

# Histogram for all Iris Setosa characteristics 
series1 = np.array(IrisSetosa['SepalLengthCm'])
series2 = np.array(IrisSetosa['SepalWidthCm'])
series3 = np.array(IrisSetosa['PetalLengthCm'])
series4 = np.array(IrisSetosa['PetalWidthCm'])
 
plt.hist(series1, label='Sepal Length', color= 'green', edgecolor='blue')
 
plt.hist(series2, label='Sepal Width', color = 'yellow', edgecolor='purple')

plt.hist(series3, label='Petal Length', color= 'orange', edgecolor='blue')
 
plt.hist(series4, label='Petal Width', color = 'blue', edgecolor='purple')

plt.xlabel('Measurements in Cm')
plt.ylabel('No. Irises')
plt.title('Iris Setosa All Characteristics')
plt.legend()
plt.show()

#Read Iris Versicolor
IrisVeriscolor = pd.read_csv('Iris_versicolor.csv')
IrisVeriscolor.head()

# Histogram for all Iris versicolor characteristics 
series1 = np.array(IrisVeriscolor['SepalLengthCm'])
series2 = np.array(IrisVeriscolor['SepalWidthCm'])
series3 = np.array(IrisVeriscolor['PetalLengthCm'])
series4 = np.array(IrisVeriscolor['PetalWidthCm'])
 
plt.hist(series1, label='Sepal Length', color= 'green', edgecolor='blue')
 
plt.hist(series2, label='Sepal Width', color = 'yellow', edgecolor='purple')

plt.hist(series3, label='Petal Length', color= 'orange', edgecolor='blue')
 
plt.hist(series4, label='Petal Width', color = 'blue', edgecolor='purple')

plt.xlabel('Measurements in Cm')
plt.ylabel('No. Irises')
plt.title('Iris Veriscolor All Characteristics')
plt.legend()
plt.show()

# Read Iris Virginica
IrisVirginica = pd.read_csv('Iris_virginica.csv')
IrisVirginica.head()

# Histogram for all Iris virginica characteristics 
series1 = np.array(IrisVirginica['SepalLengthCm'])
series2 = np.array(IrisVirginica['SepalWidthCm'])
series3 = np.array(IrisVirginica['PetalLengthCm'])
series4 = np.array(IrisVirginica['PetalWidthCm'])
 
plt.hist(series1, label='Sepal Length', color= 'green', edgecolor='blue')
 
plt.hist(series2, label='Sepal Width', color = 'yellow', edgecolor='purple')

plt.hist(series3, label='Petal Length', color= 'orange', edgecolor='blue')
 
plt.hist(series4, label='Petal Width', color = 'blue', edgecolor='purple')

plt.xlabel('Measurements in Cm')
plt.ylabel('No. Irises')
plt.title('Iris Virginica All Characteristics')
plt.legend()
plt.show()



    