#Sample array to find the smallest window that needs sorting
A = [4,8,6,5,9,10,15]

#keeps track where the the smallest window that needs to be sorted is
left = 0
right = 0

#initates a length variable to simplifiy process
length = len(A)

#initates max and min so far at the first and last index position of the array
maxSoFar = A[0]
minSoFar = A[length-1]

#transverses through the array from index 0 to lenth-1
for i in range(length):
    #if the current index is greater than the max thus far, change the max to the current index
    if(maxSoFar < A[i]):
        maxSoFar = A[i]

    #keeps track of the right side of the smallest window
    #only change right variable to i when the current index is less than, or not equal to, the current max
    #only changes right if the current index is smaller than the current max, which will be to the left of the number
    if A[i] < maxSoFar:
        right = i
        
#transverses through the array from length-1 to index position 0, decrementing at each iteration
for i in range(length-1,-1,-1):
    #changes min if current index position is smaller than current min
    if minSoFar > A[i]:
        minSoFar = A[i]
    #finds the smallest window to the left
    #if the current index positon is less than the current min, change left to keep track of the left side of the window
    if A[i] > minSoFar:
        left = i

#print the results of the smallest window
print(left)
print(right)