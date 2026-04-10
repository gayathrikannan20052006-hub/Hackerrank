from itertools import product
i=list(map(int,input().strip().split()))
j=list(map(int,input().strip().split()))
d= [(a,b) for a in i for b in j]
print(" ".join(str(tup)for tup in d))
