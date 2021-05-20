import random
import decimal
import matplotlib.pyplot as plt
import math

#Generates 1000 random x and y floats, rounded 2 decimals
x = [round(random.uniform(-1,1),2) for i in range(1000)]
y = [round(random.uniform(-1,1),2) for i in range(1000)]

#Initializes two filtered lists
filteredX = []
filteredY = []

#Iterates through x and y lists
for j in range(len(x)):
    #Adds to the filterd lists if the distance between x,y and 0,0 is less than 1
    if( math.sqrt(((x[j]-0)**2)+((y[j]-0)**2)) < 1):
        filteredX.append(x[j])
        filteredY.append(y[j])


#Plots the points on a scatter plot
plt.scatter(filteredX,filteredY)
plt.show()

A = ((1.2,3.4),(4.5,5.6))
print(A[0],A[1])