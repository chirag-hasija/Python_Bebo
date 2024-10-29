word = input("Enter a word: ")
words = {}
for w in word:
    words[w] = words.get(w, 0) + 1
for w in word:
    if(words[w] == 1):
        print(w)
        break





