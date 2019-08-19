n=int(input())
x=n
a=[]
while(x!=1):
    count=0
    for i in range(1,n):
        if(x%i==0):
            count+=1
    if(count==2):
        a.append(x)
    x-=1
a.sort()
if(n==2):
    print(0)
else:
    print(*a)
