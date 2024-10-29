word = input("Enter a word: ")
lis = []
ans = ""
s = set()
for w in word:
    if w not in s:
        s.add(w)
        lis.append(w)
print(ans.join(lis))