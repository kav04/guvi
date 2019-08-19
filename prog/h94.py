n=input()
x=n.split()
x=map(list,x)
for k in x:
    k.reverse()
    print("".join(k),end=" ")
