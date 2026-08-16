s = input("Enter string: ")
words = s.split()
ans = []

for word in words:
    found = False
    for x in ans:
        if x == word:
            found = True
            break

    if found == False:
        ans.append(word)

for word in ans:
    print(word, end=" ")
