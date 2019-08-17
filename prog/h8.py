def func():
    n=int(input())
    l=[int(x) for x in input().split()]
    for i in range(0,n):
        for j in range(i+1,n):
            sum=l[i]+l[j]
            for p in range(j+1,n):
                if(sum==l[p]):
                    print(l[i],l[j],sum)
op=func()
