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
            else:
                return "unique"
    return repeat
op=func()
if op=="unique":
    print("unique")
else:
    print (" ".join(op))

    
