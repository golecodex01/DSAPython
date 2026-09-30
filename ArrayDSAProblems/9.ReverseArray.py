'''
9. Reverse the array using another array 
Input: 
A = [10, 20, 30, 40, 50] 
Output: 
[50, 40, 30, 20, 10] 
'''

def reverseArray(data):
    rev=[]
    for i in range(len(data)-1,-1,-1):
        rev.append(data[i])
    print(rev)


data=list(map(int,input("Enter Elements : ").split()))
reverseArray(data)

