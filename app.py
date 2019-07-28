a,b=map(int,input().split())
m=list(map(int,input().split()))
c=0
for i in range(len(m)): 
    for j in range(i+1,len(m)): 
        if(m[i]+m[j]==b): 
            c=1 
            break
if(c): 
    print("yes")
else: 
    print("no")
