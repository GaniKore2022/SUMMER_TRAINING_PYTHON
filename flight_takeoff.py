N,p,q,r=list(map(int,input().split()))
x=[]
for i in [p,q,r]:
    for k in range(i,N+1,i):
        if k in x:
            x.remove(k)
        else:
            x.append(k)
print(len(x))
# s=0
# for i in range(1,N+1):
#     a=i%p
#     b=i%q
#     c=i%r
#     print(a,b,c)
#     if a==0 or b==0 or c==0:
#         if a==0 and b==0:
#             continue
#         elif a==0 and c==0:
#             continue
#         elif b==0 and c==0:
#             continue
#         s+=1
# print(s)