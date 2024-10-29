from functools import reduce
def sum_of(x,y):
    return x+y
sum = sum_of(3,4)
print(sum)

another_sum = lambda x,y:x+y
print(another_sum(5,9))

lis = [1,2,3,4,5]
square = lambda x:x*x
ans = map(square,lis)
print(list(ans))

ans2 = list(filter(lambda x: x%2 == 0, lis))
print(ans2)

# Reduce Function
def sum(a,b):
    return a+b
print(reduce(sum,ans2))

# passing arguments in function
l = [2,3,4,5]
