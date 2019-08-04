n=input()
l=len(n) 
count=0
for i in range(0,l):
    if not(n[i].isalnum()):
        count=count+1
print(count)
