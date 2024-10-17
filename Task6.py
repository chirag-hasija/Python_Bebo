hour = int(input("Enter Hours: "))

if(hour > 0 and hour < 23 ):
    parrotTalking = input("Enter ParrotTalking: ")
    if((hour < 7 and parrotTalking == 'True') or (hour > 20 and parrotTalking == 'True')):
        print('True')
    else:
        print('False')
else:
    print("Not a valid range")



