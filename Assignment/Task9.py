adult = input("Adult is present yes or no: ")
height = int(input('Enter height in inches: '))
if(height >= 48):
    print("True")
elif(height >= 32 and height <= 47 and adult == "yes"):
    print("True")
else:
    print("False")
