def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def maxprime(l,r):
    a=[]
    for i in range(l,r):
        if isprime(i):
            a.append(i)
    return a[-1]
x=[4,8,14,22,36,68]
s=0
for i in range(len(x)-1):
    s=s+(maxprime(x[i],x[i+1]))
print(s)