s=int(input())
lsr=[]
for i in range(0,s):
    n=int(input())
    lsr.append(n)
min=lsr[0] 
for j in range(1,s):
    if(min>lsr[j]):  
        min=lsr[j]       
print(min)
