'''
6. Take position from the user and delete that element 
Input: 
A = [10, 20, 30, 40, 50] 
Position = 2 
Output: 
[10, 20, 40, 50] 

'''

def  deleteonindex(data,index):
    for i in range(index,len(data)-1):
        data[i]=data[i+1]
    data.pop()
    print(data)

data=list(map(int,input("Enter Elements : ").split()))
x=int(input("Enter Index to Delete  : "))

deleteonindex(data,x)