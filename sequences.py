#In the for loop, the entire array is checked. This mean the program would run at O(n) length
#The entire array would need to be checked this ways as we would need to find the start and end of each sequence, increasing and decreasing
#The current index value would need to be compared to the next index value, to check if the sequence continues or if it has been broken
#As the length of the array grows, so would the time leading me to belive the program would run O(n) complexity

def increasingSequences(arr):
    largestIncreasing = 0
    tempLargest = 1
    
    for i in range(len(arr)-1):
        #print(arr[i],"<",arr[i+1])
        if(arr[i]<arr[i+1]):
            tempLargest += 1
        else:
            #print("temp:", tempLargest)
            #print("largest:", largestIncreasing)
            #print("\n")
            if(tempLargest > largestIncreasing):
                largestIncreasing = tempLargest
                tempLargest = 1
            else:
                tempLargest = 1

    return largestIncreasing

def decreasingSequences(arr):
    largestDecreasing = 0
    tempLargest = 1
    
    for i in range(len(arr)-1):
        #print(arr[i],">",arr[i+1])
        if(arr[i]>arr[i+1]):
            tempLargest += 1
        else:
            #print("temp:", tempLargest)
            #print("largest:", largestDecreasing)
            #print("\n")
            if(tempLargest > largestDecreasing):
                largestDecreasing = tempLargest
                tempLargest = 1
            else:
                tempLargest = 1

    return largestDecreasing


def sequence(list):
    longestIncrease = 1
    tempIncrease = 1
    longestDecrease = 1
    tempDecrease =1 

    #Runs through the entire array
    for i in range(len(list)-1):
        #Checks to see if the array is increasing
        if list[i] < list[i+1]:
            #reset decrease as sequence has been broken
            tempDecrease = 1
            #Keep increamenting counter so long as sequence is increasing
            tempIncrease += 1
            #As the current sequence grows, compare against the longest increasing sequence noted
            #Update the longest increasing sequence every iteration of if statement
            longestIncrease = max(longestIncrease,tempIncrease)
        #If not increasing, assumption is decreasing the array
        else:
            #Reset current increasing sequence as it has been broken
            tempIncrease = 1
            #Increament current decreasing sequence length
            tempDecrease += 1
            #Compares the current decreasing sequence with the longest before
            #Updates longest sequence to whichever is largest
            longestDecrease = max(longestDecrease,tempDecrease)

    print("Longest sequence of strictly increasing integers: ", longestIncrease)
    print("Longest sequence of strictly decreasing integers: ", longestDecrease)

A = [1,2,4,3,2,5,7,8,12,8,13,14,12,8,6,4,2,3,4] 
print("Largest strictly increasing integers: ", increasingSequences(A))
print("Largest strictly decreasing integers: ", decreasingSequences(A))
sequence(A)