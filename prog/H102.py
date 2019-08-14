n=int(input())
s=str(n)
sum=0
for i in range(0,len(s)):
    sum=sum+(int(s[i])**2)
print(sum)
