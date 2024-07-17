n,p=list(map(int,input().split()))
ap=list(map(int,input().split()))
ap.sort()
l=0
mini=float('inf')
while(l+n<=p):
    x=ap[l:l+n]
    if mini>abs(x[0]-x[-1]):
        mini=abs(x[0]-x[-1])
        ans=x
    l+=1
print(*ans)