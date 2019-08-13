n1,n2=map(int,input().split())
l=[int(x) for x in input().split()]
for i in range(0,n1):
    if(l.count(l[i])==n2):
        print(l[i])
        break
    
