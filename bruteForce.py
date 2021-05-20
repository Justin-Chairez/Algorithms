import math
import random

def brute_force(A):

    #Initialize the variable to hold the closest pair
    PairCoordinate = [(0,0),(0,0)]

    #Initialize and declare the shortest distance as infinite as to avoid errors
    shortestDistance = float("inf")

    #Runs through the entire array of tuples
    for i in range(len(A)):
        #Gets the coordinates of the first point
        xCoordinate1 = A[i][0]
        yCoordinate1 = A[i][1]
        #Moves one ahead of the current index to get the next coordinate
        for j in range(i+1,len(A)):
            #Gets the coordinates of the second point
            xCoordinate2 = A[j][0]
            yCoordinate2 = A[j][1]
            #Uses the distance formual to calculate the distance between the two points
            currentDistance = math.sqrt(((xCoordinate2-xCoordinate1)**2)+((yCoordinate2-yCoordinate1)**2))
            #If the calculated current distance is shorter than short distance kept tracked of, update the value
            if(currentDistance < shortestDistance):
                shortestDistance = currentDistance
                #Save the coordinates of the pairs
                PairCoordinate = [(A[i][0],A[i][1]),(A[j][0],A[j][1])]

    return PairCoordinate
                

A = [(0,2.1),(-1.3,4.3),(5.7,9),(-5,4),(2.4,6)]
print("Shortest Distance: ", brute_force(A))
