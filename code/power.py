s=int(input())
flag=0
if(s>1):
    while(s!=0):
        s=s/2
        if(s==2):
            flag=1
    if(flag==1):
        print("yes")
    else:
        print("no")
elif(s==1):
    print("yes")
else:
    print("no")