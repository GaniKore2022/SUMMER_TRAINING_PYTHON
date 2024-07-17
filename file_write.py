# n=int(input())
# print(any(6**i == n for i in range(1, 10)))
def rev(str):
    if len(str)==1:
        return str
    else:
        return rev(str[1:])+str[0]
str='hello'
print(rev(str))
