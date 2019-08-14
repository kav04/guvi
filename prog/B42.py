def func():
    l=input().split()
    for i in range(0,len(l)):
        if(len(l[i])==len(l[i+1]) or len(l[i])>len(l[i+1])):
            return l[i]
        else:
            return l[i+1]
print(func())
