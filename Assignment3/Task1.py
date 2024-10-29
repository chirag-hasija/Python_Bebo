word = input("Enter a word: ")
first = word.lower()
last = first[::-1]
if first == last:
    print("Palindrome")
else:
    print("Not Palindrome")