A = [3,7,4,1,8,5,6,2]

def reverse_array(a):
    end = len(a)-1
    i = 0
    middle = len(a)//2
    while(i != middle):
        a[i],a[end-i] = a[end-i],a[i]
        i += 1
    return a


print("Before reversed: ", A)
reverse_array(A)
print("After reversed: ", A)
