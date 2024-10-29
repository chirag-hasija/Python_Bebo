numbers = [1,5,3,7,9]
maxi = numbers[0]
lis = []
for i in range(len(numbers)-1):
    for j in range(len(numbers)):
        maxi = max(maxi,numbers[i]*numbers[j])
print(maxi)