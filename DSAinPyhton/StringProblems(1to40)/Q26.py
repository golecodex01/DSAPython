s = input("Enter string: ")
word = input("Enter word: ")
index = -1

for i in range(len(s) - len(word) + 1):
    match = True
    for j in range(len(word)):
        if s[i + j] != word[j]:
            match = False
            break

    if match:
        index = i
        break

print(index)
