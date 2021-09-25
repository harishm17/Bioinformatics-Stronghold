dna = input().strip()
motif = input().strip()
for i in range(0, len(dna)):
    if dna[i:i + len(motif)] == motif:
        print(i + 1, end=" ")
