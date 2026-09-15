'''

5.
 Student Grade Classification System (Python List Assignment)


A school stores student marks in a list. The system must analyze the marks and generate a **clear performance report**
by grouping students into grade categories.



Write a Python program to:

* Iterate through the list of marks
* Assign grades based on marks:

  * **>= 90 → A**
  * **>= 75 and < 90 → B**
  * **>= 50 and < 75 → C**
  * **< 50 → Fail**
* Store each category in separate lists
* Count students in each category
* Display a **final structured report (important)**

---

## 📌 Output Format (Mandatory)

Your output must be displayed exactly in this format:

```
===== STUDENT GRADE REPORT =====

A Grade Students   : [list]
B Grade Students   : [list]
C Grade Students   : [list]
Fail Students      : [list]

--------------------------------
A Count   : X
B Count   : X
C Count   : X
Fail Count: X
--------------------------------

Total Students: X
```

---

 Input

[95, 82, 67, 45, 30]

Output

```
===== STUDENT GRADE REPORT =====

A Grade Students   : [95]
B Grade Students   : [82]
C Grade Students   : [67]
Fail Students      : [45, 30]

--------------------------------
A Count   : 1
B Count   : 1
C Count   : 1
Fail Count: 2
--------------------------------

Total Students: 5

'''
marks=list(map(int,input("Enter Marks : ").split()))
A=[]
A_count=0
B_count=0
C_count=0
F_count=0

B=[]
C=[]
Fail=[]
for i in marks:
    if i>=90 and i<=100:
        A.append(i)
        A_count+=1

    elif i>=75 and i<90:
        B.append(i)
        B_count+=1
    elif i>=50 and i<75:
        C.append(i)
        C_count+=1
    else:
        Fail.append(i)
        F_count+=1

print("===== STUDENT GRADE REPORT =====")

print("A Grade Students   : ",A)
print("B Grade Students   : ",B)
print("C Grade Students   : ",C)
print("Fail  Students   : ",Fail)
print()
print("=============================")
print("A Count   : ",A_count)
print("B Count   : ",B_count)
print("C Count   : ",C_count)
print("Fail Count   : ",F_count)
