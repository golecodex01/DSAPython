'''5 Compare two strings ignoring case.
 S1 = "Test", S2 = "test" Equal (or 0) '''

s1=input("Enter s1 : ")
s2=input("Enter s2 : ")

if len(s1)==len(s2):
    flag=True
    for i in range(len(s1)):
        if s1[i].lower()!=s2[i].lower():
            flag=False
    if flag:
        print("Eqaul ")
    else:
        print("Not Equal ")

else:
    print("Not Equal ")
