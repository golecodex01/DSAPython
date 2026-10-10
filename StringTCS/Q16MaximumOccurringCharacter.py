'''
16. Find the maximum occurring character
Return the character with the highest frequency. If tied, return the one that appears first.
Test Case	Input	Expected Output
1	banana	a (3)
2	hello	l (2)
3	aabb	a (2)

'''
def find_maxOccuring(data):
    d={}
    for i in data:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    max=-1
    maxch=''
    for k,v in d.items():
        if v>max:
            max=v
            maxch=k
    print(maxch,"(",max,")")

s=input("Enter YOur String : ")
find_maxOccuring(s)