base = int(input("Enter a base: "))
exponent = int(input("Enter an exponent: "))
result = 1
for i in range(1,exponent+1):
    result *= base
print(result)