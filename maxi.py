s=int(input())
lsr=[]
for i in range(0,s):
    n=int(input())
    lsr.append(n)
max=lsr[0] 
for j in range(1,s):
    if(max<lsr[j]):  
        max=lsr[j]       
print(max)

