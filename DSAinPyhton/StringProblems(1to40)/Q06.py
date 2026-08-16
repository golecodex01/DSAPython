s = input("Enter string: ")
ans = ""
for ch in s:
    if 'a' <= ch <= 'z':
        ans += chr(ord(ch) - 32)
    else:
        ans += ch
print(ans)
