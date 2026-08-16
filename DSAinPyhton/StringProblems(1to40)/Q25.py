s = input("Enter string: ")
count = 0
inside = False

for ch in s:
    if ch != ' ' and inside == False:
        count += 1
        inside = True
    elif ch == ' ':
        inside = False

print(count)
