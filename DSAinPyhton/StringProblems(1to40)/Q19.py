s = input("Enter string: ")
max_count = 0
answer = ""

for i in range(len(s)):
    count = 0
    for j in range(len(s)):
        if s[i] == s[j]:
            count += 1

    if count > max_count:
        max_count = count
        answer = s[i]

print(answer)
