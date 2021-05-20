def c(n,k):
    numerator = 1
    denom = 1
    #Because n>k is always true, we know the largest value between n and n-k will always be n-k
    start = n-k
    #Numerator value becomes equal to n to (n-k)+1
    #For instance, c(50,3) goes from 48 t0 50
    for i in range(start+1,n+1):
        print("i value: ", i)
        numerator *= i
    #Denominator becomes the factorial of k
    for j in range(1,k+1):
        print("j value: ", j)
        denom *= j
        print("denom: ", denom)
    print(numerator,denom)
    return numerator//denom

print(c(50,3))