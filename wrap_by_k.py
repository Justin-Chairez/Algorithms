def wrap_by_k(lst, k):
    for i in range(k):
        for i in range(len(lst)-2,-1,-1):
            lst[i+1],lst[i] = lst[i],lst[i+1]
    return lst


A = [1,2,3,4,5,6,7,8]
print("List before wrap  by k: ", A)
print("Wrap by K: ", wrap_by_k(A,3))
#print("This would run at O(n) complexity as it has to transverse through the entire array")