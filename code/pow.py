s,c=[int(s) for s in input().split()]
flag=0
if(s>1):
    while(s!=0):
        s=s/c
        if(s==c):
            flag=1
    if(flag==1):
        print("yes")
    else:
        print("no")
elif(s==1):
    print("yes")
else:
    print("no")
