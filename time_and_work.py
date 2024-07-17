lst1=[(1,3),(2,5),(4,6),(6,7),(5,8),(7,9)]
lst2=[5,6,5,4,11,2]
d={}
for i,j in zip(lst1,lst2):
    d[i]=j
max_s=float('-inf')
i=0
l=[]
while(i<len(lst1)):
    j=i+1
    a=[lst1[i]]
    k=lst1[i][1]
    while(j<len(lst1)):
        if k<=lst1[j][0]:
            a.append(lst1[j])
            k=lst1[j][1]
        j+=1
    l.append(a)
    i+=1
for lst in l:
    s=0
    for t in lst:
        s+=d[t]
    max_s=max(max_s,s)
print(max_s)