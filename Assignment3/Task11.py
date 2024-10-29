word = input("Enter a word: ")
j = 0
start = 1
for i in range(j+1,len(word)):
    if(word[i] == word[j]):
        start += 1
    else:
        print(word[j],start)
        j = i
        start = 1
print(word[j],start)



