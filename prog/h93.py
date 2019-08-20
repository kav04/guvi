n=input()
x=n.split()
a=[]
b=[]
for i in x:
    a.append(len(i))
z="".join(x)
for i in range(len(z)):
    if(i%2==0):
        b.append(z[i].upper())
    else:
        b.append(z[i].lower())
w="".join(b)
for k in a:
    for h in range(0,len(w),k):
        l=w[h:h+k]
        print(l,end=" ")
    break
