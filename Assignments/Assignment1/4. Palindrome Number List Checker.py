'''


4.
Palindrome Number List Checker
Scenario

A system checks lucky numbers which are palindromes.

Requirements
Check palindrome numbers
Store palindrome numbers in list
Count palindrome numbers
Find largest palindrome
Sort palindrome list
Test Cases

Input:
[121, 131, 20, 44, 55, 100]

Output:

Palindromes: [121, 131, 44, 55]
Count: 4
Largest: 131
Sorted: [44, 55, 121, 131]


Requirements
Check palindrome numbers
Store palindrome numbers in list
Count palindrome numbers
Find largest palindrome
Sort palindrome list

'''
numbers=list(map(int,input("Enter Your Numbers : ").split()))
polindrome=[]
nonpolindrome=[]
ncount=0
pocount=0
print("Your Entered List : ",numbers)
for i in numbers:
    temp=i
    rev=0
    while i>0:
        rev=rev*10+i%10
        i=i//10
    if temp==rev:
        polindrome.append(temp)
        pocount+=1
    else:
        nonpolindrome.append(temp)
        ncount+=1

if len(polindrome)>0:
    high=polindrome[0]
    for i in polindrome:
        if i>high:
            high=i
print("Largest Polindrome : ",high)
print("Polindrome Count : ",pocount)
print("Non Polindrome Count : ",ncount)
print("List of Non Polindrome Number : ",nonpolindrome)
sortpolindrome=polindrome
for i in range(len(sortpolindrome)):
    for j in range(i,len(sortpolindrome)):
        if sortpolindrome[i]>sortpolindrome[j]:
            temp=sortpolindrome[i]
            sortpolindrome[i]=sortpolindrome[j]
            sortpolindrome[j]=temp
print("List of Polindrome in Sorted Order : ",sortpolindrome)


    
        