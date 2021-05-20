def next_permutations (arr):
    #will need to run the entire array
    length = len(arr)-1

    #when initialzing, needs to be outside of possible indexs of array
    decrease = -1

    #to store values that are to the right of the switch
    temp = []

    #start from where the index swapped, when an increase was noted
    begining = -1

    #end index position where the swapped occured
    end= len(arr)

    #starts from the end of the array and works forward
    while length > 0:
        #finds where the next value needs to be switched to give next largest permutation
        if arr[length] > arr[length-1]:
            #add current indext to values needed to be sorted
            temp.append(arr[length])
            #notes the value where decreasing number was found
            decrease = arr[length-1]
            #notes where decreasing index value was found
            begining = length-1
            #stops once we find where to change next
            break
        else:
            #if not, add this value to the current temp array to organize later
            temp.append(arr[length])
        #decrements to next position
        length -= 1
    temp.append(decrease)
    #sorts in increasing order, numbers to the left of the index where decreasing value was found
    temp.sort()
    #print("temp ", temp)
    #print("first decrease" , decrease)
    
    #finds the next largest value in the subarray, after current index value
    for i in range (len(temp)):
        #since array is sorted, next value after the decrease value is the next largest number by default
        if temp[i] > decrease:
            #places next largest value where decreasing value was found
            arr[begining] = temp[i]
            #removes next largest value from temp array
            temp.remove(arr[begining])
            break
    #returns the next largest permutation
    res = arr[0:begining+1] + temp
    return res


list5 = [8,7,9,4,1,2,3,3,5,6]
#list5 = [4,6,5,7]
print(list5)
print(next_permutations(list5))

