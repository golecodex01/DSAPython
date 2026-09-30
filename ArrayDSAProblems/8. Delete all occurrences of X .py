'''
8. Delete all occurrences of X 
Input: 
A = [10, 20, 30, 20, 40, 20] 
X = 20 
Output: 
[10, 30, 40] 
'''


def deleteALlX(data, x):
    for i in range(len(data)-1, -1, -1):
        if data[i] == x:
            data.pop(i)

    print(data)

data=list(map(int,input("Enter your Array : ").split()))
x=int(input("Enter Your Element to Delete : "))

deleteALlX(data,x)