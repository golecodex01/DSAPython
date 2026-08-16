s1 = input("Enter S1: ")
s2 = input("Enter S2: ")

if len(s1) != len(s2):
    print("Not Equal")
else:
    same = True
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            same = False
            break

    if same:
        print("Equal")
    else:
        print("Not Equal")
