from itertools import product

chars = [x for x in input().split()]
n = int(input())
chars = sorted(chars)

perm = [x for x in product(chars, repeat=n)]
for i in perm:
    print(''.join(i))
