def inversions(arrA,arrB):
    #Initalizes merged list size
    merged = []

    #Initalizes inversion counter
    #Inversions are counter as the number of value still left in the other subarray that larger than the current index value being sorted
    inversionCounter = 0

    #Initalizes index variables
    i = 0
    j = 0

    #Keeps running so long as the end of arrA and arrB hasn't been reached
    while i < len(arrA) and j < len(arrB):
        
        #Compares and adds smallest element from each array and advances the index positon
        if arrA[i] < arrB[j]:   
            merged.append(arrA[i])
            i += 1
        else:
            merged.append(arrB[j])
            #Adds to the inversion counter the numbers still larger than current index from opposing subarray
            inversionCounter += (len(arrA)+len(arrB))//2-i
            print("inversion counter: ", inversionCounter)
            print("i: ", i)
            j += 1

    #Adds remainder of subarray A, if last value added was from subarray B
    while i < len(arrA):
        merged.append(arrA[i])
        i += 1
        
    #Adds remainder of subarray B, if last value added was from subarray A
    while j < len(arrB):
        merged.append(arrB[j])
        j += 1
        inversionCounter += (len(arrA)+len(arrB))//2-i


    #Returns both the sorted array and the inversion counter
    return merged,inversionCounter



A = [2,3,5,7]
B = [0,1,4,6]
C = [1,4,7,10]
D = [2,5,8,9]

print(inversions(C,D))