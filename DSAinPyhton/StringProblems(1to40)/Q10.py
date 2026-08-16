s = input("Enter string: ")
start = 0
end = len(s) - 1

while start <= end and s[start] == ' ':
    start += 1
while end >= start and s[end] == ' ':
    end -= 1

ans = ""
for i in range(start, end + 1):
    ans += s[i]
print(ans)
