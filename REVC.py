dna = input()
comp = {'T': 'A', 'A': 'T', 'G': 'C', 'C': 'G'}
rc = ''
for x in dna:
    rc = comp[x] + rc
print(rc)
