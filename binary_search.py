import random
import time

#Initial test array
list1 = [1,3,6,7,11,12,18,21]

def binary_search(array,target):
    length = len(array)
    start = 0
    end = length-1
    #Continue searching so long as we have not reached the end
    while start <= end:
        #Split the current section of the array in half, on first call splits entire array 
        middle = (start+end)//2
        #Checks to see if middle index is the targe value
        if(target == array[middle]):
            return middle
        #If not, check to see if the target value would be on the left or right side by comparing values
        elif(target > array[middle]):
            start = middle+1
        else:
            end = middle-1
    return middle

#Makes a big list of numbers to test search algorithm
big_list = []
top = 2**26
for i in range(top):
    big_list.append(i)

start_time = time.time()
binary_search(big_list,top-1)
print("--- %s seconds ---" % (time.time()-start_time))