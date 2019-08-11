def func(n,s,x):
    for i in range(0,n):
        j=i+1
        for m in range(j,n):
            if((x[i]+x[m])==int(s)):
                return "yes"
    return "no"   
n,s=[int(x) for x in input().split()] 
x=[int(x) for x in input().split()]
print(func(n,s,x))
