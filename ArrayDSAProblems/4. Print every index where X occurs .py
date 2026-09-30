'''
4. Print every index where X occurs 
Input: 
A = [10, 20, 30, 20, 40, 20] 
X = 20 
Output: 
Indices: 1 3 5 

'''
def findindex(data,x):
    print("Indices : ",end=" ")
    for i in range(len(data)):
        if data[i]==x:
            print(i,end=" ")

data=list(map(int,input("Enter Elements : ").split()))
x=int(input("Enter Your Target to Search : "))

findindex(data,x)