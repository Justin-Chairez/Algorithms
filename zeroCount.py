def couting_zero(n):
    count = 0
    i = 5
    #Keeps running so long as n is divisable by the next power of 5
    while( n//i >= 1):
        count += n//i
        #Increases 5 by 1 power each iteration of the loop
        i *= 5
    return int(count)

n = 10
print("How many zeros does", n, "! have")
print(couting_zero(n))
#I belive this would be O(n) since the amount of times the while loops executes is dependent on how large n is