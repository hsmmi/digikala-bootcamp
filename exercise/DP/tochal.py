mod = 10**9 + 7

# Get input
def get_input():
    global n, h
    n = int(input())
    h = list(map(int, input().split()))
    pass


def solve():
    global n, h
    # dp[i][j]: total pal in arr[i:j+1] which contains h[i]
    dp = [[0] * (n) for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1

    for length in range(2, n + 1):
        for start in range(n - length + 1):
            end = start + length - 1

            dp[start][end] = dp[start][end - 1]
            if h[start] == h[end]:
                dp[start][end] += 1
                for middle in range(start + 1, end):
                    if h[start] <= h[middle]:
                        dp[start][end] = (
                            dp[start][end] + dp[middle][end - 1]
                        ) % mod

    total = 0
    for i in range(n):
        total = (total + dp[i][n - 1]) % mod

    return total


from random import randint


# Main
if __name__ == "__main__":
    global n, h
    id = 9
    while id:
        n = randint(1, 30)

        h = [randint(1, 30) for _ in range(n)]

        # write to file
        with open(f"input_{id}.txt", "w") as f:
            f.write(f"{n}\n")
            f.write(" ".join(map(str, h)))
            f.close()

        # wrute to file
        with open(f"output_{id}.txt", "w") as f:
            f.write(str(solve()))
            f.close()
        id -= 1

    pass
