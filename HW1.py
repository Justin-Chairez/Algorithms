a = [3,7,5,6,9]

#finds length of array
length = len(a)

#Creates two temp arrays for the products
FrontProduct = [0]*length
BackProduct = [0]*length

#Creates product array
ProductArray = [0]*length

#Start index at 1 to simplify multiplication of front and end product arrays
#Does not include the last multiple of FrontProduct, for example 3,670, as number is not used
#Starting at 1 allows for direct multiplication of arrays
FrontProduct[0] = 1

#Follows same principles as FrontProduct
#Allows for direct multiple of Front and Back product
BackProduct[length-1] = 1


#Finds the front product
for i in range(1,length):
    #multiples the current index position by the product found in the previous index position
    FrontProduct[i] = a[i-1] * FrontProduct[i-1]


#Finds the end product
for j in range(length-2, -1, -1):
    #starts at the end of the Back array and multiples forward
    #multiples the current index by the product of the previous index
    BackProduct[j] = a[j+1] * BackProduct[j+1]

#Finds the product array
#multiples both arrays from index 0 to the end
for i in range(length):
    ProductArray[i] = FrontProduct[i] * BackProduct[i]

print('Front')
print(FrontProduct)
print('Back')
print(BackProduct)

print('Product: ')
print(ProductArray)