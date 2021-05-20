import time
import random

def inversions(arrA,arrB):
    #Initalizes merged list size
    merged = []

    #Initalizes inversion counter
    #Inversions are counter as the number of value still left in the other subarray that larger than the current index value being sorted
    inversionCounter = 0s

    #Initalizes index variables
    i = 0
    j = 0

    #Keeps running so long as the end of arrA and arrB hasn't been reached
    while i < len(arrA) and j < len(arrB):
        
        #Compares and adds smallest element from each array and advances the index positon
        if arrA[i] < arrB[j]:   
            merged.append(arrA[i])
            i += 1
        else:
            merged.append(arrB[j])
            #Adds to the inversion counter the numbers still larger than current index from opposing subarray
            inversionCounter += (len(arrA)+len(arrB))//2-i
            #print("inversion counter: ", inversionCounter)
            #print("i: ", i)
            j += 1

    #Adds remainder of subarray A, if last value added was from subarray B
    while i < len(arrA):
        merged.append(arrA[i])
        i += 1
        
    #Adds remainder of subarray B, if last value added was from subarray A
    while j < len(arrB):
        merged.append(arrB[j])
        j += 1
        inversionCounter += (len(arrA)+len(arrB))//2-i


    #Returns both the sorted array and the inversion counter
    return merged,inversionCounter

def countInversions(arr):
    
    length = len(arr)
    
    #Base case, where subarrays have only one element in them
    if length == 0 or length == 1:
        return arr, 0
    else:
        #Finds the middle of the array
        middle = length//2

        #Splits the current array into sub arrays
        #Operates similar to binary, in divide and conquer method
        begining = arr[:middle]
        end = arr[middle:]

        #Further splits the sub array until each are of size one
        #Keeps track of left, right, and inversions when merging subarrays together

        #Splits the left subarrays in half and passes on a tuple of the subarray and inversion counter
        begining,leftInversions = countInversions(begining)

        #Splits the right subarray in half and passes on a tuple of the subarray and inversion counter
        end, rightInversions = countInversions(end)

        #Passes in the subarrays calculated above inversions where they are sorted
        merged, splitInversions = inversions(begining,end)

        #returns the merged list and the total inversions that took place
        return merged, leftInversions+rightInversions+splitInversions


B = []
for i in range(40000):
    B.append(i)
#print("Original array: ", B)
for i in range(100):
    firstRan = random.randint(0,len(B)-1)
    secondRan = random.randint(0,len(B)-1)
    B[firstRan],B[secondRan] = B[secondRan],B[firstRan]
#print("Shuffled array: ", B)

start_time = time.time()
countInversions(B)
print((time.time()-start_time))