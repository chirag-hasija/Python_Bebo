sentense = input("Enter a sentence: ")
another = sentense[::-1]
lis = another.split(" ")
for ans in lis:
    print(ans[::-1],end=" ")
