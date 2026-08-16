s = input("Enter string: ")
min_count = len(s) + 1
answer = ""

for i in range(len(s)):
    count = 0
    for j in range(len(s)):
        if s[i] == s[j]:
            count += 1

    if count < min_count:
        min_count = count
        answer = s[i]

print(answer)
