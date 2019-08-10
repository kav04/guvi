n=int(input())
lst=[int(n) for n in input().split()]
c=0
for i in range(1,n+1):
    if(i*n in lst):
        c=c+1
print(c)
