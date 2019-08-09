s=input()
sp=s.split()
for i in range(0,len(sp)):
    n=sp[i] 
    res=list(n)
    res.reverse()
    x="".join(res)
    print(x,end=" ")
