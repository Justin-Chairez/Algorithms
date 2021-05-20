import time

def find_peak(arr):
    currentIndex = 0
    #Only need to check values up until peak value is found
    #Stops while loop once the next index is less than the index the while-loop is currently on
    while( arr[currentIndex+1] > arr[currentIndex]):
        #Advance to next index position so long as it is greater than current position
        currentIndex += 1
    return currentIndex


A = [2,3,4,6,7,8,3,2]

B = [0]
for i in range(1,2**24):
    B.append(i)
B.append(0)

C = [0]
for i in range(1,2**26):
    C.append(i)
C.append(0)


start = time.time()
print(find_peak(B))
print("Time taken: ", time.time()-start)
