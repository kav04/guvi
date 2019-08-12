n=int(input())
l1=[int(x) for x in input().split()]
for i in l1:
    if(l1.count(i)==1):
        print(i)
        break
