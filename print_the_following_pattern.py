a=int(input())
r=0
for i in range(1,a+1):
    rem=i%10
    r=r*10+rem
    i=i//10
    print(r)