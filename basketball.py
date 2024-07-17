n=int(input())
k=int(input())
a=list(map(int,input().split()))
m=float('-inf')
for i in range(n-k+1):
    p=1
    cs=0
    for j in range(i,i+k):
        cs+=a[j]*p
        if p==k:
            break
        p+=1
    m=max(m,cs)
print(m)        