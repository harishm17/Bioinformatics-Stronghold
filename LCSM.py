data = {}
x = input().strip()
while x:
    if x.startswith('>'):
        fasta_id = x[1:]
        s = ''
        x = input().strip()
        while x and x[0] != '>':
            s += x
            x = input().strip()
        data[fasta_id] = s
seq = []
for x in data:
    seq.append(data[x])

short = min(seq, key=len)
for length in range(len(short), 0, -1):
    for i in range(len(short) - length + 1):
        substr = short[i:i + length]
        if all(seqs.find(substr) >= 0 for seqs in seq):
            print(substr)
            quit()
