n=int(input())
a=[]
b=[]
for i in range(n):
    k,v=input().split()
    a.append(int(k))
    b.append(v)
x=[]
for i in range(n):
    if a[i]==1:
        x.append(b[i])
    elif a[i]==2:
        if b[i] in x:
            print("True")
        else:
            print("False")
    elif a[i]==3:
        l=len(b[i])
        for w in x:
            if w[:l]==b[i]:
                print("True")
                break
        else:
            print("False")
    elif a[i]==4:
        if b[i] in x:
            x.remove(b[i])
print(x)
inp="wo"
l1=len(inp)
for i in x:
    if i[:l1]==inp:
        print(i)
inp1="sch"
l2=len(inp1)
s=set(x)
for i in s:
    if i[:l2]==inp1:
        print(i)