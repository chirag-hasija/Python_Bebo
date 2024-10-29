num = int(input("Enter a number: "))
if(num > 0 and (num%11 == 0 or num%11 == 1)):
    print("Special")
else:
    print('Not special')
