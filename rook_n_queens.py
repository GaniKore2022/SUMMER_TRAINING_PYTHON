def nqueen(r):
    if(r==n):
        return
    for c in range(n):
        if(check(r,c)):
            m[r][c]=1
            break
    return nqueen(r+1)
def check(i,j):
    if(i==u):
        return 0
    elif(j==v):
        return 0
    r=i
    c=j
    for i in range(r+1):
        if(m[i][j]==1):
            return 0
    i=r
    while(i>=0 and j>=0):
        if(m[i][j]==1):
            return 0
        i=i-1
        j=j-1
    while(r>=0 and c<n):
        if(m[r][c]==1):
            return 0
        r=r-1
        c=c+1
    return 1
    
n=8
u=1
v=3
m=[]
s=0
for i in range(n):
    m.append([0]*n)
nqueen(0)
print(m)
for row in m:
    s+=sum(row)
print(s)