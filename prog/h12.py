n,m=list(map(int,input().split()))
l=[int(x) for x in input().split()]
l=list(set(l))
l.sort()
l.reverse()
print(l[m-1])
