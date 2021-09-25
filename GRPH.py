data = {}
x = input().strip()
while x:
    if x[0] == '>':
        name = x[1:]
        s = ''
        x = input().strip()
        while x and x[0] != '>':
            s += x
            x = input().strip()
        data[name] = s
k = 3
for name in data:
    for othernames in data:
        if name != othernames and data[name][-k:] == data[othernames][:k]:
            print(name, othernames)
