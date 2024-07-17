n=4
d=2
x=[7,8,9,3]
y=[i//2 for i in x]
maxi=max(y)
for i in range(n-1,-1,-1):
    if y[i]==maxi:
        print(i+1)
        break