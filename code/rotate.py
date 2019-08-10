n,c=[int(n) for n in input().split()]
lst=[int(n) for n in input().split()]
x=(lst[c:]+lst[0:c])
y=" ".join(map(str,lst))
print(y)
