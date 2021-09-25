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
# data contains {FASTA ID: DNA}
max_id = ''
max_gc = 0
for id, dna in data.items():
    temp_gc = (dna.count('G') + dna.count('C')) / len(dna)
    if temp_gc > max_gc:
        max_id = id
        max_gc = temp_gc
print(max_id)
print(max_gc*100)
