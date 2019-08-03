def func(ind,s):
    lst=[] 
    sum=0
    for x in range(0,s):
        num=input()
        lst.append(num)
    if (ind<s):
        for i in range(0,ind):
            sum=sum+int(lst[i])
        return sum
index=int(input())
size=int(input())
op=func(index,size)
print(op)
    
