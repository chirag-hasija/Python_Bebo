lis = ['a','b','c']
lis2 = []
for i in range(len(lis)):
    lis3 = []
    lis3.append(lis[i])
    for j in range(len(lis)):
        if(lis[i] == lis[j]):
            continue
        lis3.append(lis[j])
    lis2.append(lis3)
for i in range(len(lis)):
    lis3 = []
    lis3.append(lis[i])
    for j in range(len(lis)-1,-1,-1):
        if(lis[i] == lis[j]):
            continue
        lis3.append(lis[j])
    lis2.append(lis3)
print(lis2)