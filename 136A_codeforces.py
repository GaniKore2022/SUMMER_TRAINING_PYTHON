n=4
x=[2,3,4,1]
d={}
for i in range(1,n+1):
    d[i]=x[i-1]
y={}
for i,j in d.items():
    y[j]=i
y=dict(sorted(y.items()))
print(*(list(y.values())))