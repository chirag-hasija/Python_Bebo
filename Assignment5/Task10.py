lis1 = [1,3,5,7]
lis2 = [2,4,6,8]
lis3 = []

i = 0
j = 0
while(i < len(lis1) and j < len(lis2)):
    if(lis1[i] < lis2[j]):
        lis3.append(lis1[i])
        i += 1
    else:
        lis3.append(lis2[j])
        j += 1
while (i<len(lis1)):
    lis3.append(lis1[i])
    i += 1
while(j < len(lis2)):
    lis3.append(lis2[j])
    j += 1
print(lis3)