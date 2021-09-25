n=int(input())
edges=[]
x=input()
while x:
    edges.append(x)
    x=input()

print(n-len(edges)-1)