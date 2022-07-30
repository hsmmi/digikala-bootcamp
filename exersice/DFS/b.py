n, m = map(int, input().split())
s, t = map(int, input().split())

G = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

# BFS
def BFS(source, target):
    visited = [False] * n
    visited[source] = True
    node_list = [source]
    dist = [0]
    par_index = [-1]
    i = 0
    while i < len(node_list):
        current = node_list[i]
        for w in G[current]:
            if w == target:
                ans = [w + 1]
                j = i
                while j > -1:
                    ans.append(node_list[j] + 1)
                    j = par_index[j]
                return ans[::-1]
            if not visited[w]:
                node_list.append(w)
                dist.append(dist[i] + 1)
                par_index.append(i)
                visited[w] = True
        i += 1
    return -1


ans = BFS(s - 1, t - 1)

if ans == -1:
    print("-1")
else:
    print(len(ans) - 1)
    print(*ans)
