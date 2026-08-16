s = input("Enter string: ")
words = s.split()
done = []

for word in words:
    already = False

    for x in done:
        if x == word:
            already = True

    if already == False:
        count = 0
        for x in words:
            if x == word:
                count += 1

        print(word, ":", count)
        done.append(word)
