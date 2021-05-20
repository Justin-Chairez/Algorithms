import random
import math
import matplotlib.pyplot as plt
import time

#Finds the closest pair
def closest_pair(Px, Py):

    # Base Case if there are 3 or less points
    if len(Px) <= 3:
        return bruteForce(Px)
    
    # first half of x sorted by x coordinate
    Lx = Px[:len(Px)//2] 
    # first half of y sorted by y coordinate 
    Ly = Py[:len(Py)//2] 
    # second half of x sorted by x coordinate
    Rx = Px[len(Px)//2:] 
    # second half of y sorted by y coordinate 
    Ry = Py[len(Py)//2:]  

    #Recursively calls these methdos to form a checkerboard pattern through splitting in half on the x and y axis
    #Essentially stops once there are 3 or less points in a box and finds the shortest distance from the points in that quadrant
    #Returns A tuple of (x,y) of best points on the left and right hand side
    l1, l2 = closest_pair(Lx, Ly)
    r1, r2 = closest_pair(Rx, Ry)

    #Delta is the shortest distance found on both the right and left hand side
    g = min(dist(l1, l2), dist(r1, r2))

    #Returns the best split pair from Px, Py, and delta
    #Delta assists in helping narrowing down points by eliminating those points who's distance is greater than delta
    s1, s2 = closest_split_pair(Px, Py, g)

    #Calculates which pair of points has the smallest distance
    #Compares the left, right, and split pair and finds the min
    bestDistance = min(dist(l1, l2), dist(r1, r2), dist(s1, s2))

    #Checks which pair of points the shortest distance belongs to
    if bestDistance == dist(l1, l2):
        return l1, l2
    elif bestDistance == dist(r1, r2):
        return r1, r2
    else:
        return s1, s2

#Takes in coordinates sorted by x, coordinates sorted by y, and delta
#A point is a split pair if one point is to the left and another is to the right of the median
def closest_split_pair(Px, Py, g):

    #Finds the median of the x sorted coordinates
    median = Px[len(Px)//2][0]

    #Declare and initialze the strip
    #Strip holds all the points that are within the range of delta, from both the left and right
    Sy = []
    for point in Py:
        # a pair of points is a split pair if the x coordinate of each point is in between (median - g) and (median + g)
        if median - g <= point[0] <= median + g:
            Sy.append(point)
    
    #Shortest distance thus far is delta
    bestDistance = g
    #Create temp best distance points from the coordinates, to update later
    bestPair = Px[0], Px[1]
    for i in range(len(Sy)):
        for j in range(1, min(7, len(Sy)-i)):
            #If a shorter distance is found, update distance and the points associated with it
            if dist(Sy[i], Sy[i+j]) < bestDistance:
                bestDistance = dist(Sy[i], Sy[i+j])
                bestPair = Sy[i], Sy[i+j]
    #returns a tuple of the coordinates with the shortest distance, for split pair
    return bestPair[0], bestPair[1]

#Brute force method from previous assignment
#Transverses the array, comparing each point's distance
#At most 3 points will be passed into this method
def bruteForce(Px):
    length = len(Px)
    minDistance = dist(Px[0], Px[1])
    target = (Px[0], Px[1])
    if length == 2:
        return Px[0], Px[1]
    for i in range(0, length):
        for j in range(i + 1, length):
            distance = dist(Px[i], Px[j])
            if distance < minDistance:
                minDistance = distance
                target = (Px[i], Px[j])
    return target[0], target[1]

#Distance formula
#Takes in two tuples of (x,y) format
def dist(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)


# ************HANDLES GENERATING RANDOM POINTS AND PLOTTING THEM************#

#Generates random numbers with a seed to test code
#random.seed(64)

#Holds tuples of all the points generated
all_coordinates = [] 
#Holds the x coordinates of points
x_coordinates = []
#Holds the y coordinates of points
y_coordinates = [] 


# Initalizing 64 pair of points
for i in range(10**2):

    #Generates and adds x coordinate(in range 0-10) to respective list
    x_val = round(10 * random.random(), 2)
    x_coordinates.append(x_val)
    #Generate and adds y coordinate(in range 0-10) to respective list
    y_val = round(10 * random.random(), 2)
    y_coordinates.append(y_val)
    #Adds x and y coordinates, as a tuple, to the coordinates list
    all_coordinates.append((x_val, y_val))


# Scatters all the points
plt.scatter(x_coordinates, y_coordinates)

#Sorts all coordinates by the x-value
Px = sorted(all_coordinates, key=lambda x_val: x_val[0])
#Sorts all coordinates by the y-value
Py = sorted(all_coordinates, key=lambda y_val: y_val[0])

#Findest the closest coordinate pair
start_time = time.time()
closestCoordinates = closest_pair(Px, Py)
print("Time taken: ", time.time()-start_time)

#Turns first coordinate red
plt.scatter(closestCoordinates[0][0], closestCoordinates[0][1], color = 'red')

#Turns second coordinate red
plt.scatter(closestCoordinates[1][0], closestCoordinates[1][1], color = 'red')

plt.show()