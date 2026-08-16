s = input("Enter string: ")
ch = input("Enter character: ")
count = 0

for i in range(len(s)):
    if s[i] == ch:
        count += 1

print(count)
