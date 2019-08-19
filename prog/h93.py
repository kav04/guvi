n=input()
x=n.split()
for i in x:
    for j in range(len(i)):
        if(j%2==0):
            print(i[j].upper(),end="")
        else:
            print(i[j].lower(),end="")
    print(end=" ")
