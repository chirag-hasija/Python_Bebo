day = int(input("Enter a day number: "))
vacation = input("you are on vacations yes or no: ")
if(vacation == "yes"):
    if(day == 6 or day == 0):
        print("Off")
    else:
        print("Alaram rings at 10.00")
else:
    if (day == 6 or day == 0):
        print("Alaram rings at 10.00")
    else:
        print("Alaram at 7.00")