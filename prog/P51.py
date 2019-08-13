n=int(input())
l=[int(x) for x in input().split()]
a=min(l)
l.remove(a)
b=min(l)
print(b)
