s,n=input().split()
n=int(n)
for i in range(0,len(s)):
    print(s[i:n],end=" ")
    if(n<len(s)):
        n=n+1
    else:
        break
