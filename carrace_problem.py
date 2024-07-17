s=input()
n=int(input())
res=""
for i in range(n):
    d,r=input().split()
    if d.upper()=='L':
        res+=s[int(r):]+s[:int(r)][0]
    elif d.upper()=='R':
        res+=s[-int(r):]+s[:-int(r)][0]
l=0
while(l<=len(s)-n):
    if sorted(s[l:l+n])==sorted(res):
        print("Yes")
        break
    l+=1
else:
    print("No")