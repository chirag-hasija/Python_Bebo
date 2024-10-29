aSmile = bool(input("Enter aSmile: "))
bSmile = (bool
          (input("Enter bSmile: ")))
print(type(bSmile))
print(bool(bSmile))
if(aSmile == True and bSmile == True):
    print("True")
elif(aSmile == False and bSmile == False):
    print("True")
else:
    print("False")