#determine the probability of two numbers (x,y) being relatively prime
import random

def prob(n):
    count = 0
    #Checks if two numbers are relatively prime n amount of times
    for i in range(n):
        #Generates two random numbers in range 1 to n
        num1 = random.randint(1,n)
        num2 = random.randint(1,n)
        #print("1 num: ", num1)
        #print("2 num: ", num2)

        #Uses Euclid algoirthm here
        while( num1%num2 != 0):
            num1,num2 = num2%num1,num1
        val = num2
        #print(num2)

        #If the remainder of Euclid algo is 1, this means both numbers were prime
        #Increaments counter to calculate probability later
        if( val == 1):
            count += 1

    #Returns the probability
    return count/n*100

print("The probability of prime numbers in 100 is ", prob(10000),"%")
