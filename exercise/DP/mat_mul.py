# Get input
from math import inf


def get_input():
    global n, mat
    n = int(input())
    tmp = list(map(int, input().split()))
    mat = [(tmp[i], tmp[i + 1]) for i in range(n)]
    pass


def solve():
    global n, mat

    # dp[i][j]: min cost to multiply mat[i:j+1]
    dp = [[0 for i in range(n)] for j in range(n)]

    # init dp
    for i in range(n - 1):
        dp[i][i + 1] = mat[i][0] * mat[i][1] * mat[i + 1][1]

    # dp
    for seq_len in range(3, n + 1):
        # renge [start, start + seq_len]
        for start in range(n - seq_len + 1):
            # mat[start:end]
            end = start + seq_len - 1
            dp[start][end] = inf
            for split in range(start + 1, end + 1):
                dp[start][end] = min(
                    dp[start][end],
                    dp[start][split - 1]
                    + dp[split][end]
                    + mat[start][0] * mat[split][0] * mat[end][1],
                )

    print(dp[0][n - 1])


# Main
if __name__ == "__main__":
    get_input()
    solve()
    pass
