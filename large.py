def func():
    n=int(input())
    lst=[] 
    for x in range(0,n):
        num=(input())
        lst.append(num)
    lst.sort()
    lst.reverse()
    return lst
op=func()
res=""
for i in range(0,len(op)):
    res=res+op[i] 
print(int(res))
