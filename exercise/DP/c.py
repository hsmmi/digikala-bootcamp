n = int(input())

dp = [1, 1, 1, 2, 3]

for _ in range(10**5 + 10):
    dp.append((dp[-1] + dp[-2] + dp[-3] - dp[-4]) % (10**9 + 7))

for _ in range(n):
    q = int(input())
    print(dp[q])
