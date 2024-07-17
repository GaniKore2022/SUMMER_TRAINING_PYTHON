groupSizes = [3,3,3,3,3,1,3]
l=[]
i=0
while i<len(groupSizes):
    if groupSizes[i]==1:
        l.append([i])
        i+=1
    else:
        if l and i in l[-1]:
            i+=1
            continue
        else:
            dup=[i]
        j=i+1
        while j<len(groupSizes):
            if len(dup)>=groupSizes[i]:
                l.append(dup)
                break
            if groupSizes[j]==groupSizes[i]:
                if l and j not in l[-1]:
                    dup.append(j)
                elif not l:
                    dup.append(j)
            j+=1
        i+=1
print(l)