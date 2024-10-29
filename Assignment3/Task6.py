word = input("Enter a word: ")
count = 0
for w in word:
    if(w == "a" or w == "e" or w == "i" or w == "o" or w == "u"):
        count += 1
print(count)