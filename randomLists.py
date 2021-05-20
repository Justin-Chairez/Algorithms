import random
import decimal

def randomPoints():
    x = []
    y = []

    #Generates random list x & y of 10 points each from -1 to 1
    for i in range(10):
        #rounds each generate value 2 decimal points
        randX = round(random.uniform(-1.00,1.00),2)
        x.append(randX)

        randY = round(random.uniform(-1.00,1.00))
        y.append(randY)

    #Zips the x and y coordinate to create pairs from the two randomly generated arrays
    coordinates = zip(x,y)
    return coordinates

#Assigns the generates tuplues to a list
A = list(randomPoints())

#Prints out the first and last tuple
print("First coordinate: ", A[0])
print("Last coordinate", A[len(A)-1])


#Sort the list of tuples by the x value
def sortTuples(arr):
    arr.sort(key=lambda x: x[0])
    return arr

#Prints out the ordered pairs from index 2 to index 8
Px = sortTuples(A)
for i in range(2,8,1):
    print("Position = ", i, Px[i])