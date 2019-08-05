n=input()
count1=0
count2=0
for i in range(0,len(n)):
    if(n[i]=="("):
        count1=count1+1
    else:
        count2=count2+1
if(count1==count2):
    print("yes")
else:
    print("no")
