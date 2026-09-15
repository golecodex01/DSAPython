'''

1.Student Marks Management
Create a program to store student marks in a List and perform operations.

Requirements:

Add student marks into a List
Display all marks
Find highest and lowest marks
Count students who scored above 75

Test Cases:

Input: [45, 67, 89, 90, 76] → Highest = 90, Lowest = 45, Count Above 75 = 3
Input: [10, 20, 30] → Highest = 30, Lowest = 10, Count Above 75 = 0
Input: [100, 99, 98] → Highest = 100, Lowest = 98, Count Above 75 = 3

'''
n=int(input("Enter Number of Students : "))
marks=[]
for i in range(n):
    print("Enter Marks of ",i+1," Subject : ")
    mark=int(input())
    marks.append(mark)

highest=marks[0]
lowest=marks[0]
count=0
for i in marks:

    if i>highest:
        highest=i
    if i<lowest:
        lowest=i
    if i>75:
        count+=1

print("Highest Marks : ",highest)
print("Lowest Marks : ",lowest)
print("Number of Subject having marks above 75 is : ",count)
    