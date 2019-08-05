n=int(input())
c=int(input())
st=str(n)
count=0
for i in range(0,len(st)):
    if(int(st[i])==c):
        count=count+1
print(count)
