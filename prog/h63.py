def func():
    n=int(input())
    l=[int(x) for x in input().split()]
    a=[]
    for i in range(n-1):
        max=l[i+1]
        for j in range(i+1,n-1):
            if(max<=l[j]):
                max=l[j]
        a.append(max)
    a.append(0)
    print(*a)
op=func()
