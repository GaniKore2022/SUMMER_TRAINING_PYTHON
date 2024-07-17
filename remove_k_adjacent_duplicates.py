s="iiiixxxxxiiccccczzffffflllllllllfffffllyyyyyuuuuuz"
k=5
l=list(s)
i=1
c=1
while(l):
    if l[i-1]==l[i]:
        c+=1
        i+=1
        if c>=k and i==len(l):
            index=i-k
            l[:]=l[:index]+l[i:]
            break
        elif i==len(l):
            break
    else:
        if c>=k or c%k==0:
            if i!=1:
                index=i-k
                l[:]=l[:index]+l[i:]
                i=1
                c=1
            else:
                i+=1
                if i==len(l):
                    break
        else:
            c=1
            i+=1
            if i==len(l):
                break
s="".join(l)
print(s)

