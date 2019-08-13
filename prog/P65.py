n=int(input())
l=[int(x) for x in input().split()]
lst=[] 
for i in range(0,n):
    if(l[i]<n):
        lst.append(l[i])
print(*lst)
