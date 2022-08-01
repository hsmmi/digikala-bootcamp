import sys

sys.setrecursionlimit(10**6 + 100)

n = int(input())

jadval = []

for _ in range(n):
    jadval.append(list(map(int, input().split())))

mark = [[0] * n for _ in range(n)]

direction = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]


def check(i, j):
    if i < 0 or i >= n or j < 0 or j >= n:
        return False
    return True


def DFS(i, j, c):
    if mark[i][j] > 0:
        return True, True
    mark[i][j] = c
    ghole, dare = True, True
    for a, b in direction:
        if check(i + a, j + b):
            if jadval[i + a][j + b] == jadval[i][j]:
                tmp_ghole, tmp_dare = DFS(i + a, j + b, c)
                ghole = ghole and tmp_ghole
                dare = dare and tmp_dare
            elif ghole and jadval[i + a][j + b] > jadval[i][j]:
                ghole = False
            elif dare and jadval[i + a][j + b] < jadval[i][j]:
                dare = False

    return ghole, dare


c = 1
ghole, dare = 0, 0

for i in range(n):
    for j in range(n):
        if mark[i][j] == 0:
            tmp_ghole, tmp_dare = DFS(i, j, c)
            ghole += tmp_ghole
            dare += tmp_dare
            c += 1


print(ghole, dare)
