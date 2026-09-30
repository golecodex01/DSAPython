'''
3. Count how many times X occurs 
Input: 
A = [10, 20, 30, 20, 40, 20] 
X = 20 
Output: 
20 occurs 3 times

'''

def calculateoccurance(data,x):
    count=0
    for i in data:
        if i==x:
            count+=1

    print("Occurance of ",x,"is ",count,"times ")

data=list(map(int,input("Enter Elements : ").split()))
x=int(input("Enter Your Target to Search : "))

calculateoccurance(data,x)