n,c=[int(n) for n in input().split()]
lst=[] 
for x in range(0,n):
    num=input()
    lst.append(num)
x=(lst[c:]+lst[0:c])
x=" ".join(x)
print(x)
