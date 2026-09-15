'''
3.
# Assignment: Prime Number Analyzer using List (Python)

## Scenario

A coaching institute stores student lucky numbers in a Python List.
Your task is to analyze the list and identify prime numbers for a scholarship selection process.

You must iterate through every element of the list and perform prime number analysis.

---

# Requirements

Write a Python program to:

1. Store integer values in a List
2. Iterate through all elements of the List
3. Check whether each number is prime or not
4. Display all prime numbers
5. Count total prime numbers
6. Count total non-prime numbers
7. Find the largest prime number from the List
8. Store all prime numbers into another List
9. Sort the prime numbers in ascending order and display them

---






# Test Case 1

## Input

[2, 3, 4, 5, 6, 7, 8]

## Expected Output

Prime Numbers: 2 3 5 7
Prime Count: 4
Non-Prime Count: 3
Largest Prime Number: 7
Prime List: [2, 3, 5, 7]
Sorted Prime List: [2, 3, 5, 7]

---

# Test Case 2

## Input

[10, 11, 12, 13, 14, 15]

## Expected Output

Prime Numbers: 11 13
Prime Count: 2
Non-Prime Count: 4
Largest Prime Number: 13
Prime List: [11, 13]
Sorted Prime List: [11, 13]

---

# Test Case 3

## Input

[1, 2, 17, 19, 20, 25]

## Expected Output

Prime Numbers: 2 17 19
Prime Count: 3
Non-Prime Count: 3
Largest Prime Number: 19
Prime List: [2, 17, 19]
Sorted Prime List: [2, 17, 19]

---

# Test Case 4

## Input

[4, 6, 8, 9, 10]

## Expected Output

Prime Numbers: None
Prime Count: 0
Non-Prime Count: 5
Largest Prime Number: Not Available
Prime List: []
Sorted Prime List: []

---

# Test Case 5

## Input

[29, 31, 37, 41]

## Expected Output

Prime Numbers: 29 31 37 41
Prime Count: 4
Non-Prime Count: 0
Largest Prime Number: 41
Prime List: [29, 31, 37, 41]
Sorted Prime List: [29, 31, 37, 41]

---



# Requirements

Write a Python program to:

1. Store integer values in a List
2. Iterate through all elements of the List
3. Check whether each number is prime or not
4. Display all prime numbers
5. Count total prime numbers
6. Count total non-prime numbers
7. Find the largest prime number from the List
8. Store all prime numbers into another List
9. Sort the prime numbers in ascending order and display them

---
'''

numbers=list(map(int,input("Enter Number : " ).split()))


nonprime=[]
prime=[]
primecount=0
notprimecount=0
for i in numbers:
    if i<=1:
        nonprime.append(i)
        notprimecount+=1

    else:
        count=0
        for j in range(2,((i//2)+1)):
            if i%j==0:
                count+=1
        if count==0:
            prime.append(i)
            primecount+=1
        else:
            nonprime.append(i)
            notprimecount+=1

print("All Prime NUmber List : ",prime)
print("All Prime Count ",primecount)
print("All Non Prime List ",nonprime)
print("All Non Prime Count : ",notprimecount)
if len(prime)>0:
    largest=prime[0]
    for i in prime:
        if i>largest:
           largest=i

sortprime=prime
for i in range(len(sortprime)):
    for j in range(i,len(sortprime)):
        if sortprime[i]>sortprime[j]:
            temp=sortprime[i]
            sortprime[i]=sortprime[j]
            sortprime[j]=temp

print("Short Prime Numbers : ",sortprime)
    
 