n=int(input())
sum=0
while(n!=0):
    rem=n%10
    sum=sum+(rem**2)
    n=int(n/10)
print(int(sum))
