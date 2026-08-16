s = input("Enter string: ")
word = input("Enter word: ")

for i in range(len(s) - len(word) + 1):
    match = True

    for j in range(len(word)):
        if s[i + j] != word[j]:
            match = False
            break

    if match:
        print(i, end=" ")
