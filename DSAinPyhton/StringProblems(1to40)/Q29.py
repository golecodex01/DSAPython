s = input("Enter string: ")
word = input("Enter word: ")
ans = ""
i = 0

while i < len(s):
    match = True

    if i + len(word) <= len(s):
        for j in range(len(word)):
            if s[i + j] != word[j]:
                match = False
                break
    else:
        match = False

    if match:
        i += len(word)
    else:
        ans += s[i]
        i += 1

print(ans)
