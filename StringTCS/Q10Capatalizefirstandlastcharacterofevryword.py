# '''
# 10. Capitalize the first and last character of each word
# For each word, make its first and last character uppercase; keep middle characters unchanged. Words are separated by spaces.
# Test Case	Input	Expected Output
# 1	hello world	HellO WorlD
# 2	python	PythoN
# 3	i love coding	I LovE CodinG
# '''


def captalise(data):
    new = list(data)

    if new[0] != " ":
        new[0] = new[0].upper()

    if new[len(new)-1] != " ":
        new[len(new)-1] = new[len(new)-1].upper()

    for i in range(1, len(data)-1):
        if new[i] == " ":
            if new[i-1] != " ":
                new[i-1] = new[i-1].upper()
            if new[i+1] != " ":
                new[i+1] = new[i+1].upper()

    print("".join(new))


s = input("Enter String: ")
captalise(s)
