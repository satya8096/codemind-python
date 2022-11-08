def digitsCount(n) :
    length = 0
    while (n > 0):
        length+=1
        n //= 10
    return length
def absoluteFirstLast(n, x) :
     
    i=0 
    mod=1
    while (i<x):
        mod*=10
        i+=1
    last=n%mod
    length = digitsCount(n);
    while (length != x) :
        n //= 10;
        length -= 1
    first = n
    return abs(first - last)
n,x=map(int,input().split())
print(absoluteFirstLast(n, x))