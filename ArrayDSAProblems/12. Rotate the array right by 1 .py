'''
12. Rotate the array right by 1 
Input: 
A = [10, 20, 30, 40, 50] 
Output: 
[50, 10, 20, 30, 40] 

'''

def rotateArray(data):
    ele=data[len(data)-1]
    for i in range(len(data)-1,-1,-1):
        data[i]=data[i-1]
    data[0]=ele
    print(data)

data=list(map(int,input("Enter Your Array Elements :: ").split()))
rotateArray(data)