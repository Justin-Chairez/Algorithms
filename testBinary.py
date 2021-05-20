import time

def binary_search(arr, target):
    left = 0
    right = len(arr)-1
    
    #While we haven't reached the ne
    while (left <= right):
        mid = (left+right)//2
        if (arr[mid] == target):
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

big_list = []
top = 2**22
for i in range(top):
    big_list.append(i)

start_temp = time.time()
print('practice binary search', binary_search(big_list,top-1))
print(time.time() - start_temp)
