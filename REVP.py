def rc_pal(dna):
    comp = {'T': 'A', 'A': 'T', 'G': 'C', 'C': 'G'}
    rc = ''
    for y in dna:
        rc = comp[y] + rc
    if rc == dna:
        return True
    else:
        return False


x = input().strip()
while x:
    if x[0] == '>':
        name = x[1:]
        s = ''
        x = input().strip()
        while x and x[0] != '>':
            s += x
            x = input().strip()

for i in range(4, 13):
    for z in range(len(s) - i + 1):
        if rc_pal(s[z:z + i]):
            print(z + 1, i)
