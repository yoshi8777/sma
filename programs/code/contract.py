def contracting(l):
    for i in range(1,len(l)):
        diff1=abs(l[i]-l[i-1])
        diff2=abs(l[i+1]-l[i]) if i<len(l) - 1 else None

        if diff2 is not None and diff1 <= diff2:
            return False
    return True


print(contracting([-2,3,7,2,-1]) )
print(contracting([9,2,7,3,1]))
