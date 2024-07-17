l=[1,21,5,2,50,16]
k=len(l)
l.sort()
l[k//2:]=sorted(l[k//2:],reverse=True)
print(l)