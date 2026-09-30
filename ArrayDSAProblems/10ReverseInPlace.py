'''
10. Reverse the array in-place 
Input: 
A = [10, 20, 30, 40, 50] 
Output: 
[50, 40, 30, 20, 10] 
Constraint: 
Do not use another array. 

'''
def reverseArray(data):
    start=0
    end=len(data)-1
    while start<end:
        temp=data[start]
        data[start]=data[end]
        data[end]=temp
        start+=1
        end-=1
    print(data)

data=list(map(int,input("Enter Your Array Elements :: ").split()))
reverseArray(data)
