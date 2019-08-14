n=int(input())
l=input().split()
a=[]
for i in range(len(l)):
    l[i].lower()
    a.append(l[i])
a.sort()
print(*a,end=" ")
