dna = input()
print(*(dna.count(n) for n in 'ACGT'))
