'''

1. Check whether a string is a palindrome
A palindrome reads the same forward and backward. Ignore spaces and letter case for these examples.
Test Case	Input	Expected Output
1	Madam	Palindrome
2	hello	Not Palindrome
3	nurses run	Palindrome

'''
def checkPolindrome(data):
    start=0
    end=len(data)-1
    flag=True
    while start<end:
        if data[start].lower()!=data[end].lower():
            flag=False
            break
        start+=1
        end-=1
    if flag:
        print("Palindrome String ")
    else:
        print("Not Palindome ")

word=input("Enter Your String : ").strip().replace(" ","")
checkPolindrome(word)


