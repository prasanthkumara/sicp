def frec(n):
    return((n>=3 and frec(n-1)+2*frec(n-2)+3*frec(n-3)) or n)


def fitrative(n):
    return(n<3 and n or fi(0, 1, 2, n))

def fiter(n1, n2, n3, count):
    return((count<3) and n3 or fiter(n2, n3, n3+2*n2+3*n1, count-1))
