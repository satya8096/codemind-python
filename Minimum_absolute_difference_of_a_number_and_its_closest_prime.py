def isprime(a):
    c=0
    for i in range(1,a+1):
        if a%i==0:
            c+=1
    if c==2:
        return True
    else:
        return False
a=int(input())
if isprime(a):
    print("0")
else:
    b=0
    for i in range(a+1,10000000):
        if isprime(i):
            b=i
            break
    d=0
    for j in range(a-1,0,-1):
        if isprime(j):
            d=j
            break
    if b-a>a-d:
        print(a-d)
    elif (b-a)==(a-d):
        print(a-d)
    else:
        print(b-a)