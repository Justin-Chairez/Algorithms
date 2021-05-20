import time
import random

def mergeSort(list):
    if len(list) > 1:
        #Finds the middle of the array
        middle = len(list)//2

        #Splits the current array into sub arrays
        #Operates similar to binary, in divide and conquer method
        begining = list[:middle]
        #print("Current first half: ", begining)
        end = list[middle:]
        #print("Current second half: ", end)

        #Further splits the sub array until each are of size one
        mergeSort(begining)
        mergeSort(end)

        i = 0
        j = 0
        k = 0

        #Compares the current index of each subarray and places smaller value into index
        while i < len(begining) and j < len(end):
            if begining[i] < end[j]:
                list[k] = begining[i]
                i += 1
            else:
                list[k] = end[j]
                j += 1
            k += 1
            #print("Current sorted portion", list, "\n")

        #Checks to see if there are remaining values in lists
        #Places remainder into list
        while i < len(begining):
            list[k] = begining[i]
            k += 1
            i += 1
        
        while j < len(end):
            list[k] = end[j]
            k += 1
            j += 1
    
""" A = [16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]
B = [32,31,30,29,28,27,26,25,24,23,22,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]
C = [42,50,78,58,79,89,15,92,50,56,98,46,68,62,80,99,30,15,69,56,94,43,78,33,29,84,78,31,51,90,77,90,4,32,31,30,29,28,27,26,25,24,23,22,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]

start = time.time()
mergeSort(B)
print(B)
end = time.time()
print("Time taken : ", end-start) """


#Part 1
""" list1=[]
for i in range(320000):
    list1.append(i)
list2=[random.randint(0,1000) for i in range(80000)] """

#Part 2
""" list2=[]
for i in range(320000):
    list2.append(i)
for i in range(int(len(list2)*0.10)):
    firstNum = random.randint(0,len(list2)-1)
    secondNum = random.randint(0,len(list2)-1)
    list2[firstNum],list2[secondNum] = list2[secondNum], list2[firstNum] """

#Part 3
""" list2=[random.randint(0,5000) for i in range(320000)] 
for i in range(len(list2)):
    firstNum = random.randint(0,len(list2)-1)
    secondNum = random.randint(0,len(list2)-1)
    list2[firstNum],list2[secondNum] = list2[secondNum], list2[firstNum] """

#Part 4
""" list2=[]
for i in range(320000):
    list2.append(i)
for i in range(0, len(list2), len(list2)//10):
    for j in range(i, i+len(list2)//10, 1):
        firstNum = random.randint(i, i+len(list2)//10-1)
        secondNum = random.randint(i, i+len(list2)//10-1)
        list2[firstNum],list2[secondNum] = list2[secondNum], list2[firstNum] """

#Part 5
""" list2=[]
for i in range(320000):
    list2.append(i)
for i in range(len(list2)//2):
    list2.append(random.randint(0,len(list2)-1)) """

#Part 6
list1 = []
for i in range(320000,0,-1):
    list1.append(i)


start_time = time.time()
mergeSort(list1)
print("Time taken: ", time.time()-start_time)
        