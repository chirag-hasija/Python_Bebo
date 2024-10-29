num1 = int(input("Enter a number1: "))
num2 = int(input("Enter a number2: "))
operand = input("Enter a operator: ")
if(operand == "+"):
    print(num1 + num2)
elif(operand == "-"):
    print(num1 - num2)
elif(operand == "*"):
    print(num1 * num2)
elif(operand == "/"):
    print(num1 / num2)
elif(operand == "%"):
    print(num1 % num2)
elif(operand == "//"):
    print(num1 // num2)
elif(operand == "**"):
    print(num1 ** num2)
else:
    print('Wrong operand')