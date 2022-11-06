def cover(a):
    if a< 0: 
        return 0
    if a==0: 
        return 1
    return (cover(a-1) +
            cover(a-2) +
            cover(a-3)) 
a=int(input())
print(cover(a)) 