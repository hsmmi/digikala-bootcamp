import sys

sys.setrecursionlimit(10**6 + 100)

n, m = map(int, input().split())

visited = [False] * n


def DFS(current):
    visited[current] = True
    for w in G[current]:
        if not visited[w]:
            DFS(w)


G = [[] for _ in range(n)]

v, u = map(int, input().split())

for _ in range(m):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)


DFS(v - 1)

print("YES" if visited[u - 1] else "NO")
