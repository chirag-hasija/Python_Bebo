age = int(input("Enter your age: "))
time = int(input("Enter your time between 0 and 24 hours : "))
if(time >= 20 and time <= 24):
    if(age <= 18 ):
        print("Price of ticket is $5")
    elif(age > 18 and age < 60):
        print("Price of ticket is $10")
    else:
        print("Price of ticket is $7.5")
else:
    if (age <= 18):
        print("Price of ticket is $10")
    elif (age > 18 and age < 60):
        print("Price of ticket is $20")
    else:
        print("Price of ticket is $15")




