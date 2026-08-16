s = input("Enter string: ")
ch = input("Enter character: ")
ans = ""

for x in s:
    if x != ch:
        ans += x

print(ans)
