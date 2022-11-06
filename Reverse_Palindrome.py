def rev(n):
    r=0
    while(n>0):
        i=n%10
        n=n//10
        r=r*10+i
    return r
a=int(input())
while(True):
    b=0
    b=a+rev(a)
    if(b==rev(b)):
        print(b)
        break
    else:
        a=b
        continue