import time
import random

def bubbleSort(lst):
    if(len(lst) == 1):
        return lst
    for i in range(len(lst)):
        for j in range(len(lst)-1):
            if(lst[j] > lst[j+1]):
                lst[j],lst[j+1] = lst[j+1],lst[j]
    return lst

A = [10,9,8,7,6,5,4,3,2,1]
list4=[random.randint(0,10) for i in range(800)]

start_time = time.time()
bubbleSort(list4)
print("--- %s seconds ---" % (time.time()-start_time))

#From the spread sheet data, it appears that as I doubled n the time as grew at an exponential rate
#When I graphed the various times the graph shows a n^2 grow meaning that bubble sort runs at O(n^2) on an average case