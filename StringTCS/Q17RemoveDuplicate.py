'''
17. Remove all duplicate characters
Keep only the first occurrence of each character; preserve original order.
Test Case	Input	Expected Output
1	programming	progamin
2	banana	ban
3	Hello World	Helo Wrd


'''
def remove_duplicate(data):
    new=""
    for i in range(len(data)):
        if data[i] not in new:
           new= new+data[i]
    print(new)

s=input("Enter Your String : ")
remove_duplicate(s)