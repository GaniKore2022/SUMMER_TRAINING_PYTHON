n,t=list(map(int,input().split()))
s=input()
x=list(s)
for _ in range(t):
    l=1
    while l<len(s):
        if x[l-1]=="B" and x[l]=="G":
            x[l-1],x[l]=x[l],x[l-1]
            l+=1
        l+=1
print("".join(x))
# l=1
# while l<len(s):
#     if x[l-t]=="B" and x[l]=="G":
#         x[l-t],x[l]=x[l],x[l-t]
#         l+=t
#     l+=1
# print("".join(x))