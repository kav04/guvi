def func(s,ind): 
    sum=0
    if (ind<s):
        for i in range(0,ind):
            sum=sum+int(lst[i])
        return sum
size=int(input())
lst=[]
for x in range(0,size):
    num=int(input()) 
    lst.append(num)
index=int(input()) 
op=func(size,index)
print(op)
    
