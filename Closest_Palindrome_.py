def pali(a):
    rev=0
    t=a
    while a>0:
        r=a%10
        rev=rev*10+r
        a=a//10
    if t==rev:
        return True
    else:
        return False
a=int(input())
pp=0
for i in range(a-1,0,-1):
    if pali(i):
        pp=i
        break
np=0
for j in range(a+1,10000000):
    if pali(j):
        np=j
        break
if (a-pp>np-a):
    print(np)
elif (a-pp)==(np-a):
    print(pp,np)
else:
    print(pp)