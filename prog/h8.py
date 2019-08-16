def func():
    n=int(input())
    l=[int(x) for x in input().split()]
    for i in range(0,n):
        x=i+1
        for j in range(x,n):
            sum=l[i]+l[j]
            if(sum in l):
                print("%d %d %d"%(l[i],l[j],sum))
op=func()
