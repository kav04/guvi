l=input().split()
m=len(l[0])
n=l[0]
for i in range(1,len(l)):
    if(len(l[i])>m):
        m=len(l[i])
        n=l[i]
print(n)
    
