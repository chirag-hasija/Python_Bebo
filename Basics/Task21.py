num = int(input("Enter a number: "))
divisor = 2
while(num > 1):
    if(num % divisor == 0):
        print(divisor)
        num = num//divisor
    else:
        divisor = divisor + 1
print(1)
