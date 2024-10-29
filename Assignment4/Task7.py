lis = [8,1,1,2,3,4,1,6,7]
lis2 = []
element = 1
start = 0
last = 1
for i in lis:
    if( i != element):
        last += 1
    if(i == element):
        lis2.append(start)
    start += 1
if(last > len(lis)):
    print("Null")
else:
    print(lis2)
