'''
11. Rotate the array left by 1 
Input: 
A = [10, 20, 30, 40, 50] 
Output: 
[20, 30, 40, 50, 10] 

'''
def rotateArray(data):
    pos=data[0]
    for i in range(len(data)-1):
        data[i]=data[i+1]
    data[len(data)-1]=pos
    print(data)

data=list(map(int,input("Enter Your Array Elements :: ").split()))
rotateArray(data)