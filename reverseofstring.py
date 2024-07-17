import string
lst=list(string.punctuation)
s=input()
l=0
r=len(s)-1
s1=list(s)
while(l<=r):
    if s1[l] not in lst:
        s1[l],s1[r]=s1[r],s1[l]
        l+=1
        r-=1
    elif s1[l] in lst:
        l+=1
    elif s1[r] in lst:
        r-=1
str1=''
for i in s1:
    str1+=i
print(str1)