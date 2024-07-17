arr=["on  codeforces ","beta round is running","   a rustling of keys" ]
vow=['a','e','i','o','u']
flag=0
for i in range(len(arr)):
    c=0
    arr[i]=arr[i].strip()
    for j in arr[i]:
        if j in vow:
            c+=1
    if i==0:
        if c!=5:
            flag=1
            break
    elif i==1 :
        if c!=7:
            flag=1
            break
    elif i==2 :
        if c!=5:
            flag=1
            break
    if flag==1:
        break
if flag==0:
  print("yes")
else:
  print("no")