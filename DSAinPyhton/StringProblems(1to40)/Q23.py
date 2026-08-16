s = input("Enter string: ")

for i in range(len(s)):
    count = 0
    for j in range(len(s)):
        if s[i] == s[j]:
            count += 1

    already = False
    for j in range(i):
        if s[i] == s[j]:
            already = True

    if count == 2 and already == False:
        print(s[i])
