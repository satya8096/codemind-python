def mega(a):
    c=0
    for i in range(1,a+1):
        if a%i==0:
            c+=1
    if c==2:
        while a>0:
            r=a%10
            a=a//10
            c1=0
            for j in range(1,r+1):
                if r%j==0:
                    c1+=1
        if c1==2:
            print("Mega Prime")
            
        else:
            print("Not Mega Prime")
    else:
        print("Not Mega Prime")
a=int(input())
mega(a)