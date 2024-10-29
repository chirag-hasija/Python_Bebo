word = input("Enter a word1: ")
word2 = input("Enter a word2: ")
dict = {}
dict2 = {}
if(len(word) != len(word2)):
    print("Not a Anagram")
else:
    w1 = word.lower()
    w2 = word2.lower()
    if(w1 == w2):
        print("The word is a Anagram")
    else:
        for w in word:
            count = 0
            for i in range(len(word)):
                if w == word[i]:
                    count = count + 1
            dict[w] = count
        for w in word2:
            count = 0
            for i in range(len(word2)):
                if w == word2[i]:
                    count = count + 1
            dict2[w] = count
    for w in word:
        if(dict[w] != dict2[w]):
            print("The word is not Anagram")
print("anagram")


