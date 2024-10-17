num = int(input("Enter a number: "))
result = 1
if(num > 0):
    for i in range(1,num+1):
        result = result * i
else:
    print('Not a +ve number')
print(result)
