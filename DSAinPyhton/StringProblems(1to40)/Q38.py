s = input("Enter string: ")
words = []
word = ""

for ch in s:
    if ch != ' ':
        word += ch
    else:
        if word != "":
            words.append(word)
            word = ""

if word != "":
    words.append(word)

for i in range(len(words) - 1, -1, -1):
    print(words[i], end=" ")
