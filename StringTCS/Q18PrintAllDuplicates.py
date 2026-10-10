'''
18. Print all duplicate characters
Print each character that occurs more than once, once only, in order of first appearance.
Test Case	Input	Expected Output
1	programming	r, g, m
2	banana	a, n
3	abcdef	No duplicates

'''
def print_duplicate(data):
    d={}
    for i in  data:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for k,v in d.items():
        if v>1:
            print(k,end=" ")

s=input("Enter Your String : ")
print_duplicate(s)

        
