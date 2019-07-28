a=input()
b=input()
l=[]
for i in b: 
    l.append(i)
if(len(b)==len(a)): 
    for i in range(len(a)):
        k=ord(a[i])-ord('a')+1       
        l[i]=ord(b[i])+k
for i in l:
    if i>ord('z'): 
        i=i-ord('z')+ord('a')-1
    print(chr(i),end="")
