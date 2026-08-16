s = input("Enter string: ")
old = input("Old character: ")
new = input("New character: ")
ans = ""

for ch in s:
    if ch == old:
        ans += new
    else:
        ans += ch

print(ans)
