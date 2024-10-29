def display():
    print("hello")

# passing argument
def display_argu(msg):
    print("Hello "+msg)
display()
display_argu("sir")

# passing multiple arguments
def multi_ple(a,b,c):
    print(a+b+c)
multi_ple(1,2,3)

# astrick argument

sum =0
def asterick_argu(*a):
    global sum
    for x in a:
        sum += x
    print(sum)

asterick_argu(1,2,3,4,5)