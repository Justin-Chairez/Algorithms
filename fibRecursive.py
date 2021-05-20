
def fib(numberOfTerms):
    if(numberOfTerms <= 1):
        return numberOfTerms
    else:
        return fib(numberOfTerms-1)+fib(numberOfTerms-2)

for i in range(10):
    print(fib(i))