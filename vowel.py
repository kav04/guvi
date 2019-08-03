def func(a): 
    lst=["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"] 
    if a.isalpha():
        if a in lst:
            print("Vowel")
        else:
            print("Consonant")
    else:
        print("Invalid")
n=input()
op=func(n)
   
