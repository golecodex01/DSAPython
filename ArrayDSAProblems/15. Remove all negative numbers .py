'''
15. Remove all negative numbers 
Input: 
A = [10, -5, 20, -3, 40, -8] 
Output: 
[10, 20, 40]

'''

def removeAllNEgetive(data):
    pos=[]
    for i in data:
        if i>=0:
            pos.append(i)
    print(pos)
   

data=list(map(int,input("Enter Your Array Elements :: ").split()))
removeAllNEgetive(data)

