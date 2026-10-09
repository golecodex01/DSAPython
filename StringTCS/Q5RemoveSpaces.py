'''
5. Remove spaces from a string
Remove ordinary space characters; keep other characters unchanged.
Test Case	Input	Expected Output
1	Hello World	HelloWorld
2	I love Python	IlovePython
3	NoSpaces	NoSpaces



'''
def remove_space(data):
    new=""
    for i in data:
        if i!=" ":
            new+=i
    print("After Removing the Spaces :  ",new)

s=input("Enter String : ")
remove_space(s)
