import time
import random

def inversions(arr):

    count = 0
    length = len(arr)

    #loops through the entire array
    for i in range(length):
        #runs from the next value after i until the end of the list
        for j in range(i+1,length):
            #If the next value is greater than the current value, add to counter
            if(arr[i] > arr[j]):
                count += 1

    return count

A = [1,20,6,4,5]
B = [8,4,2,1]
C = [3,2,1,5,10,6,4,8,7,9]
D = [4,2,1,7,6,5,3,0]
#print(inversions(D))

B = []
for i in range(8000):
    B.append(i)
#print("Original array: ", B)
for i in range(50):
    firstRan = random.randint(0,len(B)-1)
    secondRan = random.randint(0,len(B)-1)
    B[firstRan],B[secondRan] = B[secondRan],B[firstRan]
#print("Shuffled array: ", B)

start_time = time.time()
print("Couting inversions: ", inversions(A))
print((time.time()-start_time))

