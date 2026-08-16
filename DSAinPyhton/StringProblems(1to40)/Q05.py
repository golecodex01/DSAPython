s1 = input("Enter S1: ")
s2 = input("Enter S2: ")

if len(s1) != len(s2):
    print("Not Equal")
else:
    same = True
    for i in range(len(s1)):
        a = s1[i]
        b = s2[i]

        if 'A' <= a <= 'Z':
            a = chr(ord(a) + 32)
        if 'A' <= b <= 'Z':
            b = chr(ord(b) + 32)

        if a != b:
            same = False
            break

    if same:
        print("Equal")
    else:
        print("Not Equal")
