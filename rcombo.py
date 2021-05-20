def next_combo(A,n):
    arrLength = len(A)
    currentIndex = arrLength

    #checks the current last element in a sample of A
    #If that value is less than the last value in the larger list,n, we return that index positon as where the switch needs to occur
    while(A[currentIndex-1] == n-arrLength+currentIndex):
        currentIndex += -1
        #print("value of i in find: ", i)
    #print("If not equal: ", i-1)

    #Returns the position where the value needs to be increamented
    #Aka wasn't the largest possible number for that position
    j = currentIndex-1

    #Increaments the value at the current position
    #print("A[j]: ", A[j])
    A[j] += 1
    #print("A[j]: ", A[j])
    #Increases all values to the left of the switch by 1
    #Runs on the assumption values increament by 1 in the larger list of values
    for k in range(j,arrLength-1):
        A[k+1] = A[k]+1
    #Returns sample array with new combination
    return A

A = [1,2,3]
for i in range(55):
    A = next_combo(A,8)
    print(A)

