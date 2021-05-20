a = [3,7,5,6,9]

length = len(a)
FrontPosition = 0
BackPosition = length - 1
ProductPositon = 0

FrontProduct = [0]*length
BackProduct = [0]*length
Product = [0]*length

for i in range(length):
    if( i == 0 ):
        FrontProduct[i] = a[i]
    else:
        FrontProduct[i] = FrontProduct[i-1] * a[FrontPosition]
    FrontPosition += 1

for j in range(length-1,-1,-1):
    if( j == 4 ):
        BackProduct[BackPosition] = a[BackPosition]
    else:
        BackProduct[j] = BackProduct[j+1] * a[BackPosition]
    BackPosition -= 1

for i in range(length):
    if( i == 0 ):
        Product[i] = BackProduct[1]
    elif( i == length-1 ):
        Product[i] = FrontProduct[length-2]
    else:
        Product[i] = FrontProduct[ProductPositon] * BackProduct[i+ProductPositon-1]
        ProductPositon += 1

print(FrontProduct)
print(BackProduct)
print(Product)