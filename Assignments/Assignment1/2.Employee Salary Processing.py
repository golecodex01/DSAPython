'''


2.Employee Salary Processing
Store employee salaries in a List and calculate details.

Requirements:

Store salaries
Find average salary
Display salaries greater than average
Remove salaries below 15000

Test Cases:

Input: [10000, 20000, 30000] → Average = 20000, Above Average = 30000
Input: [15000, 15000, 15000] → Average = 15000
Input: [5000, 7000] → Remaining List = []






'''
salaries=list(map(int,input("Enter Salary : ").split()))
print(salaries)

avg=sum(salaries)/len(salaries)
print("Average : ",avg)

for i in salaries:
    if i>avg:
        print("Above  Average Salary is : ",i)
    if i<15000:
        salaries.remove(i)

print("Remaing Salary : ",salaries)

