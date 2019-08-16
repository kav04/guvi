n,m=map(int,input().split())
l=[int(x) for x in input().split()]
a=[]
for i in range(0,n):
    if(l[i]%2!=0):
        a.append(l[i])
print(a[m-1]) 
