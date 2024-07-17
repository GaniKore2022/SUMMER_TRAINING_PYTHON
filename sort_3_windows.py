a=list(map(int,input().split()))
for i in range(len(a)-2):
    x=a[i:i+3]
    x.sort()
    a[i:i+3]=x
print(a)