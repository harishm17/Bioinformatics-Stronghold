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

dna, subseq=data
temp=dna
inx=[0]
for char in subseq:
    i=temp.find(char)
    inx.append(inx[-1]+i+1)
    temp=temp[i+1:]
inx.pop(0)
print(*inx)