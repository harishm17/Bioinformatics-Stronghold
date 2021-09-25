mp = {}
mp["UUU"] = 'F'
mp["UUC"] = 'F'
mp["UUA"] = 'L'
mp["UUG"] = 'L'
mp["UCU"] = 'S'
mp["UCC"] = 'S'
mp["UCA"] = 'S'
mp["UCG"] = 'S'
mp["UAU"] = 'Y'
mp["UAC"] = 'Y'
mp["UAA"] = "Stop"
mp["UAG"] = "Stop"
mp["UGU"] = 'C'
mp["UGC"] = 'C'
mp["UGA"] = "Stop"
mp["UGG"] = 'W'
mp["CUU"] = 'L'
mp["CUC"] = 'L'
mp["CUA"] = 'L'
mp["CUG"] = 'L'
mp["CCU"] = 'P'
mp["CCC"] = 'P'
mp["CCA"] = 'P'
mp["CCG"] = 'P'
mp["CAU"] = 'H'
mp["CAC"] = 'H'
mp["CAA"] = 'Q'
mp["CAG"] = 'Q'
mp["CGU"] = 'R'
mp["CGC"] = 'R'
mp["CGA"] = 'R'
mp["CGG"] = 'R'
mp["AUU"] = 'I'
mp["AUC"] = 'I'
mp["AUA"] = 'I'
mp["AUG"] = 'M'
mp["ACU"] = 'T'
mp["ACC"] = 'T'
mp["ACA"] = 'T'
mp["ACG"] = 'T'
mp["AAU"] = 'N'
mp["AAC"] = 'N'
mp["AAA"] = 'K'
mp["AAG"] = 'K'
mp["AGU"] = 'S'
mp["AGC"] = 'S'
mp["AGA"] = 'R'
mp["AGG"] = 'R'
mp["GUU"] = 'V'
mp["GUC"] = 'V'
mp["GUA"] = 'V'
mp["GUG"] = 'V'
mp["GCU"] = 'A'
mp["GCC"] = 'A'
mp["GCA"] = 'A'
mp["GCG"] = 'A'
mp["GAU"] = 'D'
mp["GAC"] = 'D'
mp["GAA"] = 'E'
mp["GAG"] = 'E'
mp["GGU"] = 'G'
mp["GGC"] = 'G'
mp["GGA"] = 'G'
mp["GGG"] = 'G'
data = {}
x = input().strip()
s = ''
while x:
    if x[0] == '>':
        name = x[1:]
        s = ''
        x = input().strip()
        while x and x[0] != '>':
            s += x
            x = input().strip()
        data[name] = s
s = s.replace('T', 'U')
rnas1 = [s, s[1:], s[2:]]
rnas2 = []
comp = {'U': 'A', 'A': 'U', 'G': 'C', 'C': 'G'}
rc = ''
for x in s:
    rc = comp[x] + rc
rnas2 = [rc, rc[1:], rc[2:]]
rnas = rnas1 + rnas2
print(rnas)

prot = ''
ans = []
for rna in rnas:
    prot = ''
    for i in range(0, len(rna) - 3, 3):
        # if mp[rna[i:i + 3]] == "Stop":
        #     break
        prot += mp[rna[i:i + 3]]
    indices1 = [i for i, x in enumerate(prot) if x == "M"]
    indices2 = [i for i in range(len(prot)) if prot.startswith("Stop", i)]
    print(indices1)
    print(indices2)
    for j in range(len(indices2)):
        if j == 0:
            for x in indices1:
                if x < indices2[j]:
                    ans.append(prot[x:indices2[j]])
        else:
            for x in indices1:
                if x > indices2[j - 1] and x < indices2[j]:
                    ans.append(prot[x:indices2[j]])
for x in set(ans):
    print(x)
