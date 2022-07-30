import sys

sys.setrecursionlimit(10**6 + 100)

n = int(input())

G = [[] for _ in range(n)]

edge = []

for i in range(n):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    edge.append((a, b))
    for j in range(i):
        if edge[j][0] == a or edge[j][1] == b:
            G[i].append(j)
            G[j].append(i)

visited = [False] * n


def DFS(node):
    visited[node] = True
    for w in G[node]:
        if not visited[w]:
            DFS(w)


ans = 0

for node in range(n):
    if not visited[node]:
        ans += 1
        DFS(node)

print(ans - 1)
