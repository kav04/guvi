def func():
    n=int(input())
    lst=[] 
    for x in range(0,n):
        num=input()
        lst.append(num)
    lst.sort()
    lst.reverse()
    return lst
op=func()
print("".join(op))


