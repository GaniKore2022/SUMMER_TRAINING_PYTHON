arr=list(map(int,input().split()))
k=int(input())
a=0
b=0
c=0
for i in arr:
    r=i%3
    a+=i//3
    b+=i//3
    c+=i//3
    if r==1:
        a+=1
    elif r==2:
        a+=1
        b+=1
print(a)