'''
11. Calculate the frequency of each character
Count each character, including spaces. Display characters in the order they first appear.
Test Case	Input	Expected Output
1	banana	b: 1, a: 3, n: 2
2	Hello	H: 1, e: 1, l: 2, o: 1
3	a a	a: 2, space: 1



'''
def calculate_frequency(data):
    d={}
    for i in data:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for k,v in d.items():
        print(k ," : ",v)

s=input("Enter Your String : ")
calculate_frequency(s)