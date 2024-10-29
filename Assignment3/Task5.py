word = input("Enter a word: ")
char_Set = set()
str = ""
start = max_len = 0
for r in range(len(word)):
    while word[r] in char_Set:
        char_Set.remove(word[start])
        start += 1
    char_Set.add(word[r])
    if(r-start+1 > max_len):
        max_len = max(max_len,r-start+1)
        str = word[start:r+1]
print(max_len,str)
