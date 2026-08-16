s = input("Enter string: ")
words = s.split()
longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print(longest)
