data = []
x = input().strip()
while x:
    if x.startswith('>'):
        fasta_id = x[1:]
        s = ''
        x = input().strip()
        while x and x[0] != '>':
            s += x
            x = input().strip()
        data.append(s)

dna1, dna2=data
n=len(dna1)

transition=0
transversion=0
for i in range(n):
    if dna1[i]!=dna2[i]:
        if sorted(list(dna1[i]+dna2[i]))==list('AG') or sorted(list(dna1[i]+dna2[i]))==list('CT'):
            transition+=1
        else:
            transversion+=1
print(transition/transversion)