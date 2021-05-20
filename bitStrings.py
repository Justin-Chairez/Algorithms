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


    #Returns combination array with new indexes
    return A

def bitString(arr):
    #In this sample program, we know the bit string is of length 8
    zeros = [0,0,0,0,0,0,0,0]

    #Create counter to loop through Zero array
    i = 0
    #Create counter to loop through combination from next_Combo method
    j = 0


    #runs through the combinations index and makes changes
    while( i < len(zeros) and j < len(arr) ):
        #Changes zero at appropriate index from combinations function, to a 1
        #Needs -1 as to correct the index position beig examined
        if(arr[j]-1 == i):
            zeros[i] = 1
            j += 1
        i += 1
        
    #Returns next combination of bit string
    return zeros


#Prints out the first combination, out of 56, of C(A,n)
A = [1,2,3]
print("positions of 1: ", A)
print(bitString(A), "\n")

#Prints out all 55 combinations of C(A,n)
for i in range(55):
    #Gives the next combination of A choose n
    #In this case, each combination is position in an 8-bit String that needs to be converted to a 1
    A = next_combo(A,8)
    print("positions of 1: ", A)
    #Passes current combination into bitString to generate next bit string
    print(bitString(A), "\n")
