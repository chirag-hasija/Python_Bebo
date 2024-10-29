n = int(input("Enter a number: "))
outsideMode = input('Outside mode is on or off: ')
if(n >= 0 and n <= 10):
    if(outsideMode == 'on'):
        if(n <= 1 or n >= 10):
            print('True')
        else:
            print('False')
    else:
        if(n >= 0 or n <= 10):
            print('True')
        else:
            print('False')
else:
    print('Not a valid range')