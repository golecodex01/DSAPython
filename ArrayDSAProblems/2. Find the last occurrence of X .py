'''
2. Find the last occurrence of X 
Input: 
A = [10, 20, 30, 20, 40] 
X = 20 
Output: 
Last occurrence of 20 = index 3 
'''

def lastOccurance(data,target):
    for i in range(len(data)-1,-1,-1):
        if data[i]==target:
            print("Last occurrence of ",target,"= index ",i )

data=list(map(int,input("Enter Elements : ").split()))
x=int(input("Enter Your Target to Search : "))

lastOccurance(data,x)

            
