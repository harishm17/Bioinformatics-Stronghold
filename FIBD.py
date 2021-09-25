n, m = map(int, input().split())
ans = [1, 1, 1]
for i in range(3, n + 1):
    ans.append(ans[i - 1] + ans[i - 2])
    if i > m:
        ans[i] -= ans[i - m - 1]
print(ans[n])
