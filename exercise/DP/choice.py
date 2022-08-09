maxn = 2000 + 10
mod = 10**9 + 7
choice = [[0 for _ in range(maxn)] for _ in range(maxn)]

for i in range(1, maxn):
    choice[i][0] = 1
    choice[i][i] = 1
    choice[i][1] = i
    choice[i][i - 1] = i

for i in range(4, maxn):
    for j in range(2, i - 1):
        choice[i][j] = (choice[i - 1][j] + choice[i - 1][j - 1]) % mod

q = int(input())
for _ in range(q):
    r, n = map(int, input().split())
    print(choice[r][n])
