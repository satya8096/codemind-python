n=int(input())
a=list(map(int,input().split()))
mi=a[0]
j=1
while j<n:
    if a[j]%mi==0:
        j+=1
    else:
        mi=a[j]%mi
print(mi)