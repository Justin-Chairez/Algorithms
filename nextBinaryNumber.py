def nextBinary(b):
    #Declares a string to return the next binary number
    returnString = ""
    #Converts binary string to a list for easier access
    binaryNum = list(b)

    #Runs from the end to the start for changing each binary number
    for i in range(len(binaryNum)-1,-1,-1):
        #print("current i: ", i)
        #print("current number state: ", binaryNum)

        #Checks if the current index is 1 and not at the last index
        #Converts 1 to 0
        if(binaryNum[i] == '1' and i != 0):
            binaryNum[i] = '0'

        #If a 0 is found, convert to 1 and end program cause no other changes can happen to the left side
        elif(binaryNum[i] == '0'):
            binaryNum[i] = '1'
            #Converts list to a string with no spacing between each char
            returnString = ''.join(binaryNum)
            return returnString

        #Checks if 1 is found at the last index
        #Adds a 1 to the front in the case binary number is all 1s
        #Changes the 0 index of the original num to 0 
        elif(binaryNum[i] == '1' and i == 0):
            binaryNum[i] = '0'
            binaryNum.insert(0,'1')
        #print("current number after state: ", binaryNum)

    #Converts list back to a string with no seperators between each char
    returnString = ''.join(binaryNum)
    return returnString


A = "111"
print("Current binary num is: ", A)
print("Next binary num is: ", nextBinary(A))