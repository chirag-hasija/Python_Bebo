lis = [[8,1,6],[3,5,7],[4,9,2]]
sum = 0
ans = True
for i in range(len(lis[0])):
    sum += lis[0][i]
for i in range(len(lis)):
    another_sum = 0
    if(ans == False):
        break
    for j in range(len(lis[i])):
        another_sum += lis[i][j]
    if(another_sum != sum):
        print("Not a magic Square")
        ans = False
        break
    third_sum = 0
    for j in range(len(lis[i])):
        third_sum += lis[j][i]
    if(third_sum != sum):
        print("Not a magic Square")
        ans = False
        break
    fourth_sum = 0
    for j in range(len(lis[i])):
        if(i == j):
            fourth_sum += lis[i][j]
    if (third_sum != sum):
        print("Not a magic Square")
        ans = False
        break
else:
    print("Its a magic square")



