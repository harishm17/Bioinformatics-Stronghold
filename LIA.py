import math

k, n = map(int, input().split())
P = 2 ** k
prob = 0
for i in range(n, P + 1):
    prob += (math.factorial(P) / (math.factorial(i) * math.factorial(P - i))) * (0.25 ** i) * (.75 ** (P - i))
print(prob)
