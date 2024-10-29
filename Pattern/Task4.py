n = 7
start = 1
for i in range(n):
    print(" "*(n-i-1),end="")
    print("*"*(2*i+1),end="")
    print()
j = 1
for i in range(n-1,0,-1):
    print(" "*(j),end="")
    print("*"*(2*i-1),end="")
    j += 1
    print()


