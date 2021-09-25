# a, b, c, d, e, f = map(int, input().split())
# print(2 * (a + b + c) + 1.5 * d + e)
print(sum(a * b for a, b in zip([2, 2, 2, 1.5, 1, 0], map(int, input().split()))))
