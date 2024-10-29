rows = 7
spaces = rows//2
print(spaces)
start = 1
star = 1
for i in range(0,rows):
    for j in range(0,spaces):
        print(" ",end =" ")
    for k in range(0,start):
        print(star,end=" ")
    print("")
    star = 1
    if(i < 3):
        start += 2
        spaces -= 1
    else:
        start -= 2
        spaces += 1


