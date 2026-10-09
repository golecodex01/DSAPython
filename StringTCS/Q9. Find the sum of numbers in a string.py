'''
9. Find the sum of numbers in a string
Add every individual digit in the string.
Test Case	Input	Expected Output
1	a1b2c3	Sum: 6
2	Room 204	Sum: 6
3	No digits	Sum: 0


'''
def find_sum(data):
    sum=0
    for i in data:
        if i.isnumeric():
            sum=sum+int(i)
    print(sum)

s=input("Enter Your String : ")
find_sum(s)
