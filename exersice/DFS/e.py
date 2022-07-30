import sys

sys.setrecursionlimit(10**6 + 100)

n = int(input())

G = [[] for _ in range(n)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)


mark = [0] * n

q = int(input())

for _ in range(q):
    person = int(input())
    mark[person - 1] = 2


def BFS(node):
    mark[node] = 1
    node_list = [node]
    dist = [0]
    i = 0
    ans = []
    ans_dist = -1
    while i < len(node_list):
        current = node_list[i]
        for w in G[current]:
            if mark[w] == 2:
                if ans == []:
                    ans_dist = dist[i]
                    ans.append(w + 1)
                elif dist[i] == ans_dist:
                    ans.append(w + 1)
            elif mark[w] == 0:
                node_list.append(w)
                dist.append(dist[i] + 1)
                mark[w] = 1
        i += 1
    return sorted(ans)

ans = BFS(0)
print(ans[0])
