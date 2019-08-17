from itertools import permutations
n=input()
per=permutations(n)
for i in per:
    print(*i,sep="")
