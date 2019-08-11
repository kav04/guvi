n=int(input())
r=[int(x) for x in input().split()]
for i in range(0,n):
    a=r[i]
    r.remove(r[i])
    prod=1
    for j in r:
        prod*=j
    print(prod,end=" ")
    r.insert(i,a)
