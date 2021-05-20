import math

x = 1234
y = 5678

n = int(math.log10(x)+1)

a = int(x // 10**(n/2))
b = int(x % 10**(n/2))
c = int(y // 10**(n/2))
d = int(y % 10**(n/2))



def karatsuba(x,y):
    global count
    count = count + 1
    print("x : ", x)
    print("y : ", y)
    print("\n")

    #Base case
    if x < 10 or y < 10:
        return x*y
        
    #Figures out to divide the number in half, based on how many digits it has
    maxNumofDigits = max(int(math.log10(x+0.001)+1),int(math.log10(y+0.001)+1))
    numOfDivisons = int(maxNumofDigits//2)

    #Dividing x into first half
    xA = int(x // 10**numOfDivisons)
    print("xA: ", xA)
    #Dividing x into second half
    xB = int(x % 10**numOfDivisons)
    print("xB: ", xB)

    #Dividing y into first half
    yC = int(y // 10**numOfDivisons)
    print("yC: ", yC)
    #Dividng y into second half
    yD = int(y % 10**numOfDivisons)
    print("yD: ", yD)

    #Defines the different steps involved in step 4
    #Each one of these calls is a recursive call
    AC = karatsuba(xA,yC)
    BD = karatsuba(xB,yD)
    ABCD = karatsuba(xA + xB, yC + yD)
    S4 = ABCD-BD-AC

    print('xa + xb: ', xA + xB)
    print('yc + yd: ', yC + yD)

    return int(AC*(10**(numOfDivisons*2)) + S4*(10**numOfDivisons) + BD)

count = 0
print("Result: ", karatsuba(1234,5678))
print(count)
