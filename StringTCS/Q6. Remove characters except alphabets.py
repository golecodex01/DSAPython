'''
6. Remove characters except alphabets
Keep only English letters A–Z and a–z.
Test Case	Input	Expected Output
1	Hello123!	Hello
2	CSE@2026	CSE
3	Hi, Mohit.	HiMohit



'''
def  remove_ch(s):
    new=""
    for i in s:
        if i.isalpha():
            new+=i
    print(new)

s=input("Enter Your String : ")
remove_ch(s)
