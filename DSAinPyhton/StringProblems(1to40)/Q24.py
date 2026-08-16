s = input("Enter string: ")
unique = True

for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if s[i] == s[j]:
            unique = False
            break

if unique:
    print("True")
else:
    print("False")
