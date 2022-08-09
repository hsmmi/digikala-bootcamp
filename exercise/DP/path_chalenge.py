# Import

# Functions

# Get input
def get_input():
    global n, m, mat
    n, m = map(int, input().split())

    mat = [list(map(int, input().split())) for _ in range(n)]


def solve():
    global n, m, mat
    dp_to_right = [[0] * m for _ in range(n)]
    dp_to_left = [[0] * m for _ in range(n)]
    dp_sum_to_left = [[0] * m for _ in range(n)]

    # Initial values
    for row in range(m):
        dp_sum_to_left[row][0] = mat[row][0]

    for row in range(n):
        for col in range(1, m):
            dp_sum_to_left[row][col] = (
                dp_sum_to_left[row][col - 1] + mat[row][col]
            )

    dp_to_right[0][0] = mat[0][0]
    dp_to_left[0][0] = mat[0][0]
    for col in range(1, m):
        dp_to_right[0][col] = dp_sum_to_left[0][col - 1] + mat[0][col]
        dp_to_left[0][col] = dp_sum_to_left[0][col - 1] + mat[0][col]

    # Bottom-up
    for row in range(1, n):
        dp_to_right[row][0] = (
            min(dp_to_right[row - 1][0], dp_to_left[row - 1][0]) + mat[row][0]
        )
        dp_to_left[row][m - 1] = (
            min(dp_to_left[row - 1][m - 1], dp_to_right[row - 1][m - 1])
            + mat[row][m - 1]
        )

        for col in range(1, m):
            dp_to_right[row][col] = (
                min(
                    dp_to_right[row - 1][col],
                    dp_to_right[row][col - 1],
                    dp_to_left[row - 1][col],
                )
                + mat[row][col]
            )

        for col in range(m - 2, -1, -1):
            dp_to_left[row][col] = (
                min(
                    dp_to_left[row - 1][col],
                    dp_to_left[row][col + 1],
                    dp_to_right[row - 1][col],
                )
                + mat[row][col]
            )

    return min(dp_to_right[n - 1][m - 1], dp_to_left[n - 1][m - 1])


# Main
if __name__ == "__main__":
    get_input()
    ans = solve()
    print(ans)
    # print(path[n - 1][m - 1])
    pass
