'''
12. Find non-repeating characters
Print characters that occur exactly once, in their original order.
Test Case	Input	Expected Output
1	swiss	w
2	hello	h, e, o
3	aabbcde	c, d, e


'''

def non_repeating(data):
    d={}
    for i in data:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for k,v in d.items():
        if v==1:
            print(k ," : ",v)

s=input("Enter Your String : ")
non_repeating(s)