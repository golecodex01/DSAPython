'''
5. Delete the element at index 3 and shift left 
Input: 
A = [10, 20, 30, 40, 50] 
Delete: index 3 
Output: 
[10, 20, 30, 50] 

'''
def  deleteonindex(data,index):
    for i in range(index,len(data)-1):
        data[i]=data[i+1]
    data.pop()
    print(data)

data=list(map(int,input("Enter Elements : ").split()))
x=int(input("Enter Index to Delete  : "))

deleteonindex(data,x)