sentense = input("Enter a sentence: ")
lis = sentense.split(" ")
dict = {}
for ans in lis:
    dict[ans] = dict.get(ans, 0) + 1
print(dict)