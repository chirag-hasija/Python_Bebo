word = input("Enter a word: ")
dict={}
for w in word:
    count = 0
    for i in range(len(word)):
        if w == word[i]:
            count = count + 1
    dict[w]=count
print(dict)
