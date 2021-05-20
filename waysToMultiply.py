import math
import time

def c(n,k):
    numerator = 1
    denom = 1
    #Because n>k is always true, we know the largest value between n and n-k will always be n-k
    start = n-k
    #Numerator value becomes equal to n to (n-k)+1
    #For instance, c(50,3) goes from 48 t0 50
    for i in range(start+1,n+1):
        numerator *= i
    #Denominator becomes the factorial of k
    for j in range(1,k+1):
        denom *= j
    return numerator//denom

def ways_to_multiply(n):
    #Using formula from book
    waysToMultiply = c((2*n),n)//(n+1)
    return waysToMultiply

def ways_to_multiplyDynamic(n):
    
    #base case we know that occur with 0 or 1 number
    if n == 0 or n == 1:
        return 1
    
    #creates and initialzes array list to hold previous combinations possability
    numsofMultiples = [0]*(n+1)

    #Declares known base cases
    numsofMultiples[0] = 1
    numsofMultiples[1] = 1

    #begins calculating the next combination after known base case up until n+1
    for i in range(2,n+1):
        #calculates next term by multiplying the first term by the last known term
        #continues this pattern by moving the first number index forward and moving the second number index back 1
        #adds products to the current index position to calculate proper number of multiplication
        for k in range(i):
            #print("k-value: ", k)
            numsofMultiples[i] += numsofMultiples[k] * numsofMultiples[i-k-1]
    return numsofMultiples[n]

count=0
def ways_to_multiplyRecursivly(n):
    global count
    count += 1

    #Base case of what is known since the 0 term and 1 term is 1
    if n <= 1:
        return 1

    #initalize res
    res = 0
    for i in range(n):
        #starts at lowest bound and the largest bound, n-1, and multiples them together
        #sums up the result at each step
        res += ways_to_multiplyRecursivly(i) * ways_to_multiplyRecursivly(n-i-1)

    return res

#print("Dynamic time: ")
#start_time = time.time()
print(ways_to_multiplyDynamic(3))
#print((time.time()-start_time))

#print("Recursive time: ")
#start_time = time.time()
print(ways_to_multiplyRecursivly(3))
#print((time.time()-start_time))

print("counter: ", count)
