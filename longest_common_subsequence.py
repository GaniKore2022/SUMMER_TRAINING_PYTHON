text1="oxcpqrsvwf"
text2="shmtulqrypy"
maxi=float('-inf')
c=0
n1=len(text1)
n2=len(text2)
ind=-1
if n1<=n2:
    for i in text1:
        if i in text2:
            if text2.index(i)>ind:
                ind=text2.index(i)
                c+=1
                maxi=max(c,maxi)
            else:
                ind=text2.index(i)
                c=1
else:
    for i in text2:
        if i in text1:
            if text1.index(i)>ind:
                ind=text1.index(i)
                c+=1
                maxi=max(c,maxi)
            else:
                ind=text1.index(i)
                c=1
print(maxi)