n=int(input())
l=[int(x) for x in input().split()]
l.sort()
a=[]
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if(abs(l[i]-l[j])==1):
            a.append(l[i])
            a.append(l[j])
a=set(a)
print(len(a))
