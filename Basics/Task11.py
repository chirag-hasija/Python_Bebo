you = int(input("Enter a number: "))
date = int(input("Enter a date: "))
if((you>= 0 and you < 10) and (date >= 0 and date < 10)):
    if(you <=2 or date <= 2 ):
        print("No", 0)
    elif(you >= 8 or date >= 8):
        print("true", 2)
    else:
        print("Maybe",1)
else:
    print("Not a valid Range",False)