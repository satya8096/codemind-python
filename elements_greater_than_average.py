n=int(input())
a=list(map(int,input().split()))
b=sum(a)//n
count=0
for i in a:
    if i>=b:
        count+=1
print(count)