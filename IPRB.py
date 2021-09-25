k, m, n = map(int, input().split())
print((k * m + n * k + (m * n / 2.0) + (k * (k - 1) / 2.0) + (m * (m - 1) / 2) * (3.0 / 4.0)) / (
        (k * m + n * k + m * n) + (k * (k - 1) / 2.0) + (m * (m - 1) / 2.0) + (n * (n - 1) / 2.0)))
