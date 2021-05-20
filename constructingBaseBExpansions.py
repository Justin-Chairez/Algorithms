import math

def expand(number,base):
    #Returns a new string of output that will be reversed
    expanded = ""
    quotient = number
    k = 0
    while( quotient != 0):
        remainder = quotient%base
        quotient = quotient//base
        #Adds remainder to string, but first converts it to a string
        expanded += str(remainder)
    return expanded[::-1]

print(expand(351,2))