n, m = map(int, input().split())

jadval = [list(map(int, input().split())) for _ in range(n)]

total_sum = 0

for i in range(n):
    for j in range(m):
        total_sum += jadval[i][j]

dp = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n - 1, -1, -1):
    for j in range(m - 1, -1, -1):
        if i == n - 1 and j == m - 1:
            dp[i][j] = jadval[i][j]
        elif j == m - 1:
            dp[i][j] = dp[i + 1][0] + jadval[i][j]
        else:
            dp[i][j] = dp[i][j + 1] + jadval[i][j]

max_sum = dp[0][0]

sub_sum = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        sub_sum[i][j] = 0
        if i == n - 1 and j == m - 1:
            sub_sum[i][j] = total_sum
        elif i == n - 1:
            sub_sum[i][j] = total_sum - dp[0][j + 1]
        elif j == m - 1:
            sub_sum[i][j] = total_sum - dp[i + 1][0]
        else:
            sub_sum[i][j] = (
                total_sum - dp[0][j + 1] - dp[i + 1][0] + dp[i + 1][j + 1]
            )

        if sub_sum[i][j] > max_sum:
            max_sum = sub_sum[i][j]

print(max_sum)
