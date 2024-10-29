lis = [[1,2,3],[4,5,6],[7,8,9]]
lis2 = []
for i in range(len(lis)):
    lis3 = []
    for j in range (len(lis[i])-1,-1,-1):
        lis3.append(lis[j][i])
    lis2.append(lis3)

print(lis2)