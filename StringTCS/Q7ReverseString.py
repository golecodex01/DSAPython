'''
7. Reverse a string
Reverse all characters, including spaces and punctuation.
Test Case	Input	Expected Output
1	hello	olleh
2	Python 3	3 nohtyP
3	aB@12	21@Ba


'''
def reverseString(s):
    data=list(s)
    start=0
    end=len(data)-1
    while start<end:
        temp=data[start]
        data[start]=data[end]
        data[end]=temp
        start+=1
        end-=1
    
    print("Reversed String : ","".join(data))


s=input("Enter Your String : ")
reverseString(s)
