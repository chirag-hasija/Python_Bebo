num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if((num1 >13 and num1 <19 ) and(num2 >13 and num2 <19) and (num3>13 and num3 <19)):
    print("False")
elif((num1>13 and num1<19) or (num2>13 and num2<19) or (num3>13 and num3<19)):
    print("True")
else:
    print("False")