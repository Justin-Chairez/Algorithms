def euclid(x,y):
    while( x%y != 0):
        x,y = y%x,x
        #temp = x%y
        #x = y
        #y = temp
    return y

print(euclid(61,91))