np=int(input())
mp=list(map(int,input().split(" ")))
l=[]
while(len(mp)!=0): 
    if len(mp)>1: 
        l.append(max(mp))
        l.append(min(mp)) 
        mp.remove(max(mp)) 
        mp.remove(min(mp)) 
    else: 
        l.append(max(mp)) 
        mp.remove(max(mp))
for i in l: 
    print(i,end=" ") 
