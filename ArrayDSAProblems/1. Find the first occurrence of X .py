'''
1. Find the first occurrence of X 
Input: A = [10, 20, 30, 20, 40] X = 20 
Output: First occurrence of 20 = index 1 

'''
def firstOccurance(data,target):
    for i in range(len(data)):
        if data[i]==target:
            print("First Occurance of ",target,"= index ",i)
            break


data=list(map(int,input("Enter Elements : ").split()))
x=int(input("Enter Your Target to Search : "))

firstOccurance(data,x)

