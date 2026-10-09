'''
4. Remove all vowels from a string
Remove a, e, i, o, u in both uppercase and lowercase.
Test Case	Input	Expected Output
1	Education	dctn
2	Hello World	Hll Wrld
3	AEIOUxyz	xyz


'''
def remove_vowel(data):
    new=""
    for i in data:
        if i.lower() not in "aeiou":
            new=new+i
    print("After Removing the Vowels : ",new)

s=input("Enter Your String : ")
remove_vowel(s)