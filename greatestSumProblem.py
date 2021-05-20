A = [10,-12,4,8,6,-20,2,4]

sum = 0
left = 0
right = 0

#Starts at the beginning of the array
for i in range(len(A)):
    #Starts at the end of the array
    for j in range(len(A)-1,-1,-1):
        #Creates a temporary sum to hold the sum of each sub array
        tempSum = 0
        for x in range(i,j+1):
            tempSum += A[x]
        #As i and j move, it compares the sums between them and finds where it is the greatest
        if(tempSum>sum):
            sum = tempSum
            left = i
            right = j

print(sum)
print(left)
print(right)


def largest_subarray_sum(arr):
    currentMax = 0
    max_sum = arr[0]

    #Essentially keeps adding values to the right to check whether it takes away from the sum or adds to it
    for i in range(len(arr)):
        #Checks to see if the current index position, makes the current sum larger
        currentMax = max(arr[i],arr[i]+currentMax)
        #Checks if the current sum is greater than the current max_sum by seeing which is larger
        max_sum = max(max_sum,currentMax)
    return max_sum

print(largest_subarray_sum(A))