s = input("Enter string: ")
ch = input("Enter character: ")
index = -1

for i in range(len(s)):
    if s[i] == ch:
        index = i

print(index)
