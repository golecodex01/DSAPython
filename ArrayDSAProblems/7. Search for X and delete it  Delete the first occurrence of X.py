'''
7. Search for X and delete it 
Delete the first occurrence of X. 
Input: 
A = [10, 20, 30, 20, 40] 
X = 20 
Output: 
[10, 30, 20, 40] 

'''
def deleteFirstOccurance(data,x):
    

    for i in range(x, len(data)-1):
          data[i] = data[i+1]

    data.pop()
    print(data)

data=list(map(int,input("Enter your Array : ").split()))
x=int(input("Enter Your Element to Delete : "))

deleteFirstOccurance(data,x)
