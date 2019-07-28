np=int(input())
m=list(map(int,input().split(" ")))
d={}
for key in m: 
    d[key]=m.count(key) 
l=[]
for key,values in d.items():
    if(d[key]==1): 
        print(key) 
        break
