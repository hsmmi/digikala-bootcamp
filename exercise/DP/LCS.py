# Get input
def get_input():
    global str1, str2
    str1 = input()
    str2 = input()
    pass


def rec_pri(dp: list, par: list, str1: str, str2: str, i: int, j: int):
    if i == -1 or j == -1:
        return ""
    i2 = par[i][j][0]
    j2 = par[i][j][1]
    if dp[i][j] == dp[i2][j2] + 1:
        return rec_pri(dp, par, str1, str2, i2, j2) + str1[i]

    if i2 == -1 and j2 == -1:
        return str1[i]

    return rec_pri(dp, par, str1, str2, i2, j2)


def LCS(str1, str2):
    # dp[i][j] = LCS(str1[:i], str2[:j])
    dp = [[0 for _ in range(len(str2))] for _ in range(len(str1))]
    par = [[None for _ in range(len(str2))] for _ in range(len(str1))]

    # init dp
    dp[0][0] = 1 if str1[0] == str2[0] else 0
    par[0][0] = (-1, -1)
    for i in range(1, len(str1)):
        if str1[i] == str2[0]:
            dp[i][0] = 1
            par[i][0] = (-1, -1)
        else:
            if dp[i - 1][0] == 1:
                dp[i][0] = 1
                par[i][0] = (i - 1, 0)

    for j in range(1, len(str2)):
        if str1[0] == str2[j]:
            dp[0][j] = 1
            par[0][j] = (-1, -1)
        else:
            if dp[0][j - 1] == 1:
                dp[0][j] = 1
                par[0][j] = (0, j - 1)

    for i in range(1, len(str1)):
        for j in range(1, len(str2)):
            if str1[i] == str2[j]:
                max_tmp = max(dp[i - 1][j - 1] + 1, dp[i - 1][j], dp[i][j - 1])
                if max_tmp == dp[i - 1][j - 1] + 1:
                    par[i][j] = (i - 1, j - 1)
                elif max_tmp == dp[i - 1][j]:
                    par[i][j] = (i - 1, j)
                elif max_tmp == dp[i][j - 1]:
                    par[i][j] = (i, j - 1)
                else:
                    print("Error: max_tmp")
                dp[i][j] = max_tmp
            else:
                if dp[i - 1][j] >= dp[i][j - 1]:
                    dp[i][j] = dp[i - 1][j]
                    par[i][j] = (i - 1, j)
                else:
                    dp[i][j] = dp[i][j - 1]
                    par[i][j] = (i, j - 1)
    return dp[-1][-1], rec_pri(
        dp, par, str1, str2, len(str1) - 1, len(str2) - 1
    )


def solve():
    max_len, path = LCS(str1, str2)
    print(max_len)
    print(path)
    pass


# Main
if __name__ == "__main__":
    get_input()
    solve()
    pass
