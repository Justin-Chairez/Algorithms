import time
import random
import math


def findMaxLoop(A):
    n = len(A)
    m = A[0]
    for i in range(1,n):
        if A[i]>m:
            m=A[i]
    return m

num_rands=10**6
upper_bound=10**num_rands

sumx = 0
sumxSq = 0
for i in range(9):
    A=[random.randint(0,upper_bound) for i in range(num_rands)]

    st=time.time()
    findMaxLoop(A)
    time_diff=time.time()-st
    sumx += time_diff

    sumxSq += time_diff**2

    print(time_diff)

average = sumx/9
var = sumxSq-9*average**2

print()
print(average, math.sqrt(var))
