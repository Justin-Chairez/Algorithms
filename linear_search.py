import time

list1 = [1,3,6,7,11,12,18,21]

def linear_search(nums,target):
    i=0
    notFound = False
    #While we have not found the target value, continue loop
    while notFound!=True:
        #If the target value is found, kill the loop and return the index position
        if(target == nums[i]):
            notFound = True
        #If not found, advance through the list by one index position
        else:
            i += 1
    return i

big_list = []
top = 2**21
for i in range(top):
    big_list.append(i)

start_time = time.time()
linear_search(big_list,top-1)
print("--- %s seconds ---" % (time.time()-start_time))