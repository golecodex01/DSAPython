s = input("Enter string: ")
old = input("Old word: ")
new = input("New word: ")
ans = ""
i = 0

while i < len(s):
    match = True

    if i + len(old) <= len(s):
        for j in range(len(old)):
            if s[i + j] != old[j]:
                match = False
                break
    else:
        match = False

    if match:
        ans += new
        i += len(old)
    else:
        ans += s[i]
        i += 1

print(ans)
