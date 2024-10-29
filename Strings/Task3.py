str = "Python"
index = 3
if(index == len(str)):
    print(str[:index-1])
elif(index == 0):
    print(str[1:])
else:
    print(str[0:index]+str[index+1:])



