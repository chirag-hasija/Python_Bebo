str = "Python is a programming language"
# print(str.title())
# print(len(str))
# another = str.lower()
# lis = another.split(" ")
# print(lis)
# for ans in lis:
#     s = ans[0:1]
#     b = s.upper()
#     result = b + ans[1:]
#     print(result,end=" ")
result = ""
capital = True
for s in str:
    if(s == " "):
        result += s
        capital = True
    elif(capital):
        result += s.upper()
        capital = False
    else:
        result += s.lower()
print(result)


