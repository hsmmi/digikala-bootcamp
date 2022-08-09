from cmath import inf


n, m = map(int, input().split())
jadval = [list(map(int, input().split())) for _ in range(n)]

to_top = [[0 for _ in range(m)] for _ in range(n)]

for i in range(m):
    to_top[0][i] = jadval[0][i]

for i in range(1, n):
    for j in range(m):
        to_top[i][j] = to_top[i - 1][j] + jadval[i][j]


def max_sub_sum(arr: list):
    pre_max, max_sum = 0, 0
    total_max = -inf
    for num in arr:
        pre_max = max_sum
        max_sum = max(pre_max + num, num)
        total_max = max(total_max, max_sum)

    return total_max


max_req = 0


def sum_between_cols(i: int, j: int):
    "include row i, j"
    if j > i:
        i, j = j, i

    if j == 0:
        return to_top[i]

    sum_between = []
    for k in range(m):
        sum_between.append(to_top[i][k] - to_top[j - 1][k])
    return sum_between


for c1 in range(n):
    for c2 in range(c1 + 1):
        sum = sum_between_cols(c1, c2)
        max_req = max(max_req, max_sub_sum(sum))

print(max_req)
