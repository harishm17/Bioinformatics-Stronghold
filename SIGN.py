from itertools import permutations,product

import numpy as np

n=int(input())
num=[]
for i in range(1,n+1):
    if i!=0:
        num.append(i)

perm=permutations(num,n)
perm=list(perm)
sign=[-1,1]
signs=list(product(sign,repeat=n))

all=[]
for i in perm:
    for j in signs:
        all.append(np.multiply(np.array(i),np.array(list(j))))
print(len(all))
for i in all:
    print(*i)