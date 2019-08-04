n=input()
l=len(n) 
count=0
for i in range(0,l):
    if(n[i]==" "):
        count=count+1
op=l-count
print(op)
