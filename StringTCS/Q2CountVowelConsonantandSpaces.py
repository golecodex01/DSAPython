'''
2. Count vowels, consonants, and spaces
Count English letters only as vowels/consonants; count literal spaces separately. Ignore digits and punctuation.
Test Case	Input	Expected Output
1	Hello World	Vowels: 3, Consonants: 7, Spaces: 1
2	AEIOU xyz	Vowels: 5, Consonants: 3, Spaces: 1
3	Python 3.14	Vowels: 1, Consonants: 5, Spaces: 1


'''


def  count_vowel_con_space(data):
    vowel=0
    con=0
    space=0
    for i in data:
        
        if i.isalpha():
            if i.lower() in "aeiou":
               vowel+=1
            else:
                con+=1
        if i==" ":
            space+=1
    print("Your String : ",data)
    print("Vowel Count : ",vowel)
    print("Consonants Count : ",con)
    print("Space Count : ",space)


data=input("Enter String : ")
count_vowel_con_space(data)

