
#Handles algo using division
A = [1,2,3,4,5]
n = len(A)
Aprod = [0]*n
p = 1
for i in range(n):
    p *= A[i]
for i in range(n):
    Aprod[i] = p//A[i]
print(Aprod)

#Handles algo using nested loops
A = [1,2,3,4,5]
n = len(A)
Aprod = [0]*n
for i in range(n):
    p = 1
    for j in range(n):
        if i != j:
            p *= A[j]
            Aprod[i] = p
print(Aprod)


