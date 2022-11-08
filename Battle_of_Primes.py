def isprime(c):
    for i in range(c+1,100000):
        c1=0
        for j in range(1,i+1):
            if i%j==0:
                c1+=1
        if c1==2:
            return i
            break
a=int(input())
b=int(input())
c=a+b
print(isprime(c)-c)