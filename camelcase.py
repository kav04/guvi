s=input()
print(s[0].upper(),end="")
for i in range(1,len(s)):
    if(s[i]!=" "):
        print(s[i].lower(),end="")
    else:
        print(s[i])
        print(s[i+1].upper(),end="")
        
    