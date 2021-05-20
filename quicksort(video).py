import random
import time

def quicksort(A, left, right):
    if left >= right:
        return
    pivot = A[left]  #Change this variable to change where the pivot occurs
    index = partition(A, left, right, pivot)
    # recursively call on left and right
    quicksort(A, left, index-1)
    quicksort(A, index, right)
    return A

def partition(A, left, right, pivot):
    #Keeps checking so long as the end of the list has not been reached
    while left <= right:
        #Checks if the left side of the pivot has a value greater than the pivot
        while A[left] < pivot:
            left = left + 1
        #Checks if the right side of the pivot has a value less than the pivot
        while A[right] > pivot:
            right = right - 1
        #Switches values when a value greater than the pivot is on the left side
        #and when a value less than the pivot is on the right side
        if left <= right:
            A[left], A[right] = A[right], A[left]
            left = left + 1
            right = right - 1
    return left

#Part 1
list1=[]
for i in range(320000):
    list1.append(i)
list2=[random.randint(0,1000) for i in range(10)]

#Part 2
list2=[]
for i in range(40000):
    list2.append(i)
for i in range(int(len(list2)*0.05)):
    firstNum = random.randint(0,len(list2)-1)
    secondNum = random.randint(0,len(list2)-1)
    list2[firstNum],list2[secondNum] = list2[secondNum], list2[firstNum]

#Part 3
list2=[random.randint(0,1000) for i in range(320000)] 
for i in range(len(list2)):
    firstNum = random.randint(0,len(list2)-1)
    secondNum = random.randint(0,len(list2)-1)
    list2[firstNum],list2[secondNum] = list2[secondNum], list2[firstNum]

#Part 4
list2=[]
for i in range(320000):
    list2.append(i)
for i in range(0, len(list2), len(list2)//10):
    for j in range(i, i+len(list2)//10, 1):
        firstNum = random.randint(i, i+len(list2)//10-1)
        secondNum = random.randint(i, i+len(list2)//10-1)
        list2[firstNum],list2[secondNum] = list2[secondNum], list2[firstNum]

#Part 5
list2 = []
n = 8000
for i in range(n):
    list2.append(i)  # sorted list

# looking at last 10% (add to front and end)
for i in range(int(len(list2)*.10)):
    temp = list2[int(len(list2)-len(list2)*.1): int(len(list2))]
    list2.insert(0, random.randint(temp[0], temp[len(temp)-1]))


#Part 6
list1 = []
for i in range(320000,0,-1):
    list1.append(i)


start_time = time.time()
quicksort(list2,0,len(list2)-1)
print("Time taken: ", time.time()-start_time)
