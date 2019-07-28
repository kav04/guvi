r=input()
j=0
for i in range(len(r)): 
    if(r[j]<r[i]):
        print(r[i:]) 
        break
