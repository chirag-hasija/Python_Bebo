lis = [5,4,3,2]
product = 1
for l in lis:
    product *= l
lis2 = []
for l in lis:
    lis2.append(product//l)
print(lis2)

