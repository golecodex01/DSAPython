'''4Compare two strings (case-sensitive). 
S1 = "Test", S2 = "test" Not Equal (or non-zero value)
'''
s1=input("Enter S1: ")
s2=input("Enter S2: ")
count=0
if len(s1)==len(s2):
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            break
        else:
            count=count+1

    if count==len(s1):
        print("Equal ")
    else:
        print("Not Equal ")


else:
    print("Not Equal ")



