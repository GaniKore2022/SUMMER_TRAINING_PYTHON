d={"(":")","[":"]","{":"}"}
s=input()
x=[]
for i in range(len(s)):
    if x:
        if x[-1] in d.keys():
            if s[i] in d.keys():
                x.append(s[i])
            else:
                if d[x[-1]]==s[i]:
                    x.pop()
                else:
                    break
        else:
            break
    else:
        x.append(s[i])
if not x:
    print("True")
else:
    print("False")