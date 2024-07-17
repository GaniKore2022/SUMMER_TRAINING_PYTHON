def evens_odds(lst1,lst2,e,o,i):
    if i==len(lst1):
        return e,o
    if lst1[i]%2==0:
        e.append(lst1[i])
    if lst2[i]%2!=0:
        o.append(lst2[i])
    return evens_odds(lst1,lst2,e,o,i+1)
# def adding(e,o,n1,n2,s,i,j):
#     if i==n1-1 and j==n2:
#         return s
#     if j==n2:
#         return adding(e,o,n1,n2,s,i+1,0)
#     else:
#         s.append(e[i]+o[j])
#     return adding(e,o,n1,n2,s,i,j+1)
def adding(e,o,n1,n2,s,k,i,j):
    if i==n1-1 and j==n2:
        k.append(sum(s))
        return k
    if j==n2:
        k.append(sum(s))
        return adding(e,o,n1,n2,[],k,i+1,0)
    else:
        s.append(e[i]+o[j])
    return adding(e,o,n1,n2,s,k,i,j+1)
    
lst1=[6,3,2,9,4,7]
lst2=[8,7,5,3,6,9]
e,o=evens_odds(lst1,lst2,[],[],0)
n1=len(e)
n2=len(o)
print(adding(e,o,n1,n2,[],[],0,0))            

# for i in range(len(lst1)):
#     if lst1[i]%2==0:
#         e.append(lst1[i])
#     if lst2[i]%2!=0:
#         o.append(lst2[i])
# s=[]
# for i in e:
#     for j in o:
#         s.append(i+j)
# print(s)