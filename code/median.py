n=int(input())
l1=[int(x) for x in input().split()]
l1.sort()
med=((n+1)//2)
print(l1[med-1])
