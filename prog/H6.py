def func():
    n=int(input())
    l=[int(x) for x in input().split()]
    a=[]
    for i in range(0,n):
        if(l[i] not in a):
            a.append(l[i])
        else:
            print(l[i])
            break
op=func()
