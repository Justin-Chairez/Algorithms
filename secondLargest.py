def second_largest(arr):
    #Initialize and declare values
    maxSoFar = arr[0]
    secondLargest = arr[0]

    #Start loop at index one since we assume maxSoFar and secondLargest elements are index 0
    for i in range(1,len(arr)):
        print("Curent value: ", arr[i])
        print("max so far: ", maxSoFar)

        #If the current index is larger than the maxSoFar
        #Make the old max the second largest element
        #Make the new max the current index
        if(arr[i] > maxSoFar):
            secondLargest = maxSoFar
            print("Second largest: ", secondLargest)
            maxSoFar = arr[i]
            print("New max: ", maxSoFar)

        #Accounts for if the max has already been found, but the second largest value is later in the array
        if (arr[i] > secondLargest and arr[i] < maxSoFar):
            secondLargest = arr[i]

    return secondLargest
        


A = [4,7,2,3,9,1,6,0]
B = [12,35,1,10,34,1]
C = [10,5,10]
D = [10,11,18,54,100,67,1234,1010,89,7,77,90,45]
print("The second largest element: ", second_largest(D))