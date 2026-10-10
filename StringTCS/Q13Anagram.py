'''
13. Check whether two strings are anagrams
Ignore spaces and letter case. Anagrams contain the same letters with the same frequencies.
Test Case	Input	Expected Output
1	listen / silent	Anagram
2	Dormitory / dirty room	Anagram
3	hello / world	Not Anagram
'''
def checkAnagram(data1,data2):
    if len(data1)!=len(data2):
        return False
    else:
        d1={}
        d2={}
        for i in data1:
            if i in d1:
                d1[i]+=1
            else:
                d1[i]=1

        for i in data2:
            if i in d2:
                d2[i]+=1
            else:
                d2[i]=1
        if d1==d2:
            return True
        else:
            return False

s1=input("Enter S1 : ")


s2=input("Enter S2 : ")   

if checkAnagram(s1,s2):
    print("Anagram ")
else:
    print("Not Anagram ")