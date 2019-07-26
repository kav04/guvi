def func():
    num=int(input())
    lst=[]
    repeat=[] 
    for x in range(num):
        n=input()
        lst.append(n)
    lst.sort()
    for i in range(0,num):
        k=i+1
        for j in range(k,num):
            if lst[i]==lst[j] and lst[i] not in repeat :
                repeat.append(lst[i])
    return repeat
op=func()
print (" ".join(op))
    
