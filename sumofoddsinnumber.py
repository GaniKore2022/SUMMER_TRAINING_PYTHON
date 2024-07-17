def rsum(n,r):
    r=n%10
    if r==0:
        return 0
    if r%2!=0:
        return r+rsum(n//10,r)
    else:
        return rsum(n//10,r)
n=int(input())
print(rsum(n,0))