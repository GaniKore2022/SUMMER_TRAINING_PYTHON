def pf(n,a,k):
    if n==0:
        return -1
    f=[]
    while k%2 == 0:
        f.append(2)
        k= k//2
    for i in range(3,int(k**0.5)+1,2):
        while k%i == 0:
            f.append(i)
            k=k//i
    if k>2:
        f.append(k)
    if f[-1]>=n:
        return 0
    d={}
    for i in f:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    s=0
    for i,j in d.items():
        s+=(j*a[i])
    return s
n=int(input())
a=list(map(int,input().split()))
k=int(input())
print(pf(n,a,k))