def ai_equals(arr):
    #Finds the middle value of the current array
    midIndex = len(arr)//2
    #Checks if the middle index is equal to the middle value
    if ( midIndex == arr[midIndex] ):   
        return midIndex
    #If the middle index is less than the middle value, checks left side
    #Since index increases by 1, if index is less than middle the right side values will always be greater
    elif( midIndex < arr[midIndex] and len(arr) > 1):
        return ai_equals(arr[:midIndex])
    #If the middle index is greater than middle value, check right side
    elif( midIndex > arr[midIndex] and len(arr) > 1):
        return ai_equals(arr[midIndex:])
    #If middle value does equal middle index, no such value exists
    else:
        return -1


A=[-4,-3,1,2,8,9,10,11,12,14,18,19,22,50,51]
print("Position is: ", ai_equals(A))
    