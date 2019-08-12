m=int(input())
n=[int(x) for x in input().split()] 
a=min(n)
b=max(n)
a1=n.index(a)
a2=n.index(b)
print(a1+1,a2+1)
