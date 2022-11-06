def isprime(a):
    for i in range(a+1,100000):
        c=0
        for j in range(1,i+1):
            if i%j==0:
                c+=1
        if c==2:
            return i
            break
a=int(input())
b=int(input())
c=a+b
print(isprime(c)-c)