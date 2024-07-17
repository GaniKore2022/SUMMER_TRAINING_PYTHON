n=int(input())
x=[]
for i in range(n):
    x.append(list(map(str,input().split())))
print(x)
s=input()
l=0
flag=0
k=0
while(l<n):
    for i in range(n):
        if k<len(s) and x[i][l]!=s[k]:
            flag=1
            break
        elif k>=len(s):
            break
        k+=1
    if flag==1:
        break
    else:
        l+=1
if flag==0:
    print("Yes")
else:
    print("No")