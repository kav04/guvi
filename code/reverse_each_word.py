n=input()
op="" 
for i in range(0,len(n)):
    if(n[i]==" "):
        r=list(op)
        r.reverse()
        res="".join(r)
        print(res,end=" ")
        op=""
    else:
        op=op+n[i]
   
