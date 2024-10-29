sentense = input("Enter a sentence: ")
lis = sentense.split(" ")
max = 0
for word in lis:
    if(max < len(word)):
        max = int(len(word))
for word in lis:
    if(len(word) == max):
        print(word)
        break