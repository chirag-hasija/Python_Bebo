speed = int(input("Enter a speed in km/h: "))
birthday = input("Enter a birthday yes or no: ")
if(birthday == "yes"):
    if(speed <= 65):
        print(0)
    elif(speed <= 85):
        print(1)
    else:
        print(2)
else:
    if(speed <= 60):
        print(0)
    elif (speed <= 80):
        print(1)
    else:
        print(2)