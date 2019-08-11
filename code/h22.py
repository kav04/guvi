import numpy
n=int(input())
r=[int(x) for x in input().split()]
for i in range(0,n):
    a=r[i]
    r.remove(r[i])
    print(numpy.prod(r),end=" ")
    r.insert(i,a)
