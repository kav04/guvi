np=int(input())
mp=[]*np
for i in range(0,2**np): 
    k=[] 
    for j in range(np-1,0,-1):
        k.append(int(i/2**j)%2) 
    k.append(i%2) 
    mp.append(k) 
for i in mp: 
    s='' 
    for j in i:
        j=str(j)
        s=s+j
    print(s) 
