import sys

sys.setrecursionlimit(10**6 + 100)

# get n, m
n, m = map(int, input().split())

# get adjacency matrix
adj = [set() for _ in range(n)]

for i in range(m):
    party = list(map(int, input().split()))[1:]
    for j in range(len(party) - 1):
        a, b = party[j] - 1, party[j + 1] - 1
        adj[a].add(b)
        adj[b].add(a)

mark = [0] * n
cnt_color = [0]


def DFS(current, color):
    mark[current] = color
    cnt_color[color] += 1
    for neighbour in adj[current]:
        if not mark[neighbour]:
            DFS(neighbour, color)


color = 1

for i in range(n):
    if not mark[i]:
        cnt_color.append(0)
        DFS(i, color)
        color += 1

for i in range(n):
    print(cnt_color[mark[i]], end=" ")
print()
