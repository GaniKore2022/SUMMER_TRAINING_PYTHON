import string
strNum=input()
# for i in strNum:
#     if i not in string.digits:
#         print("False")
#         break
# else:
#     print("True")
x=''
for i in strNum:
    if i in string.digits:
        x+=i
print(x)