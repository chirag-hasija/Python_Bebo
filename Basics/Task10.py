cigars  = int(input('Enter the number of cigars: '))
weekend = input('Party going on weekend true or false: ')
if(weekend == 'false' and (cigars >= 40 and cigars < 60)):
    print("True")
elif(weekend == 'true' and cigars >= 40):
    print("True")
else:
    print("False")
