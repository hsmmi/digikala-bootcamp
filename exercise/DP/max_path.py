# Import

# Functions

# Get input
def get_input():
    global n, m, mat
    n, m = map(int, input().split())

    mat = [list(map(int, input().split())) for _ in range(n)]


def print_path(path, i, j) -> str or None:
    if path[i][j] == None:
        return ""

    if path[i][j] == "U":
        return print_path(path, i + 1, j) + "U"

    if path[i][j] == "R":
        return print_path(path, i, j - 1) + "R"

    return "error"


def solve():
    global n, m, mat
    dp = [[0 for _ in range(m)] for _ in range(n)]
    path = [["" for _ in range(m)] for _ in range(n)]

    # Initial values
    dp[n - 1][0] = mat[n - 1][0]
    path[n - 1][0] = None
    for i in range(n - 2, -1, -1):
        dp[i][0] = dp[i + 1][0] + mat[i][0]
        path[i][0] = "U"

    for j in range(1, m):
        dp[n - 1][j] = dp[n - 1][j - 1] + mat[n - 1][j]
        path[n - 1][j] = "R"

    # Bottom-up
    for i in range(n - 2, -1, -1):
        for j in range(1, m):
            dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]) + mat[i][j]
            if dp[i + 1][j] > dp[i][j - 1]:
                path[i][j] = "U"
            else:
                path[i][j] = "R"

    return dp[0][m - 1], print_path(path, 0, m - 1)


# Main
if __name__ == "__main__":
    get_input()
    max_val, path = solve()
    print(max_val)
    print(path)
    pass
