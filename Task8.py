num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
negative = input('Enter Parameter: ')
if(negative == 'True'):
    if(num1 < 0 and num2 < 0):
        print("True")
    else:
        print("False")
else:
    if((num1 < 0 and num2 >0) or (num1>0 and num2<0)):
        print("True")
    else:
        print("False")
