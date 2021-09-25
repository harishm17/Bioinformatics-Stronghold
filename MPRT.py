import urllib.request

prots = []
name = input().strip()
out = {}
while name:
    url = 'https://www.uniprot.org/uniprot/' + name + '.fasta'
    x = urllib.request.urlopen(url)
    s = ''
    for line in x:
        line = line.decode('utf-8')
        if line[0] != '>':
            s += line.strip()
    prot = s
    out[name] = []
    for i in range(len(prot) - 4):
        if prot[i] == 'N' and prot[i + 1] != 'P' and prot[i + 2] in ['S', 'T'] and prot[i + 3] != 'P':
            out[name].append(i + 1)
    name = input()
for name in out:
    if len(out[name]) != 0:
        print(name)
        print(*out[name])
