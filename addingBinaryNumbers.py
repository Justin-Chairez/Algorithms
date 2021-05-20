def add(a,b):
    if len(a) > len(b):
        length = len(a) - 1
    else:
        length = len(b) - 1
    c = 0
    for j in range(length,-1,-1):
        r = c
        if (a[j] == '1'):
            r += 1
        else:
            r += 0
        if (b[j] == '1'):
            r += 1
        else:
            r += 0
        