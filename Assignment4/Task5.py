# num = (1,2,3,4,5)
# lis = list(num)
# lis.remove(max(lis))
# lis.remove(min(lis))
# num = tuple(lis)
# print(num)
num = {1, 2, 3, 4, 5}
num_list = list(num)
max_value = num_list[0]
min_value = num_list[0]

for i in range(len(num_list)):
    if num_list[i] > max_value:
        max_value = num_list[i]
    if num_list[i] < min_value:
        min_value = num_list[i]

num_list.remove(max_value)
num_list.remove(min_value)


result = tuple(num_list)
print(result)
