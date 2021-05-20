
def addBinary(a,b):
    added = ""
    j = 0
    carryOver = 0
    #Starts from the end of the array and works to the front
    for i in range(len(a)-1,-1,-1):
        #print("a: ", a[i] , "b: ", b[i])
        #Adds one column at a time of a and b, plus carryover from previous addition
        d = (int(a[i]) + int(b[i]) + carryOver)//2
        #print("d: ", d)
        #Adds to the results string
        added += str(int(a[i]) + int(b[i]) + carryOver - 2*d)
        #print("added: ", added)

        #Takes into an account, for instance, two 4-digit numbers making a 5-digit number
        #If we've reached the end of both numbers, and we have a left over it adds it to the string
        if( i == 0 and d == 1):
            added += str(d)
        else:
            carryOver = d
            
    return added[::-1]

#Alternate way of doing this program
def addingBinary(a,b):

    #Takes into account two numbers may be of different length
    largest_len = max(len(a), len(b))
    #Adds zero to the left of the digits if need be, to make them same length
    a = a.zfill(largest_len)
    b = b.zfill(largest_len)

    added = ""
    carryOver = 0

    #Starts at the end of the array and moves forward
    for i in range(largest_len-1,-1,-1):
        #Does addition one column at a time

        #If addition of current column is zero
        if( int(a[i])+int(b[i]) + carryOver == 0 ):
            added += "0"
            carryOver = 0

        #If addition of current column is 1
        elif( int(a[i])+int(b[i]) + carryOver == 1 ):
            added += "1"
            carryOver = 0

        #If there is overflow, and digit is 2 we now have to carry over
        elif( int(a[i])+int(b[i]) + carryOver == 2 ):
            added += "0"
            carryOver = 1

        #If current row adds to 2 plus carryover is 1, we carry over a digit and make current column 1
        elif( int(a[i])+int(b[i]) + carryOver == 3):
            added += "1"
            carryOver = 1
        
    #Takes into account of an extra carryover when length of both lists have been run
    if carryOver != 0:
        added += str(carryOver)
        
    return added[::-1]
        

print(addBinary("10101010","10101011"))
print(addingBinary("10101010", "10101011"))