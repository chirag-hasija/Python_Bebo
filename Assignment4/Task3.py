dict1 = {'John': 85, 'ajay': 'ab', 'chirag': 89}
sum = 0
for i in dict1.values():
    if(type(i) == int):
        sum += i
    else:
        print(f"value is not int {i}")
print(sum)