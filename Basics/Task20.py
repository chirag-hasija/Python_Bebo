num = int(input("Enter a number: "))
digit = 0
num3 = num
while(num3 != 0):
    digit += 1
    num3 //= 10

num2 = num
sum = 0
while(num > 0):
    sum += ((num%10) **digit)
    num = num//10
if(sum == num2):
    print("Yes")
else:
    print("No")