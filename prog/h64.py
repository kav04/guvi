n=int(input())
m=[1000,500,100,50,10,1]
t=0
for i in m: 
    if(n>=i):
        no=n//i 
        t=t+no 
        n=n-no*i 
    if n==0: 
        break
if(n==0):
    print(t)
