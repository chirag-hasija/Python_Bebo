str = input("Enter a string: ")
# if(str.startswith("not")):
#     print(str)
# else:
#     print("not "+str)
length = len(str)
if(length < 3):
    print("Not"+str)
else:
    if(str[0:3] == "Not"):
        print(str)
    else:
        print("Not"+str)


