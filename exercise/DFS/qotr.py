import sys

sys.setrecursionlimit(10**6 + 100)

n = int(input())

tree = [[] for _ in range(n)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a - 1].append(b - 1)
    tree[b - 1].append(a - 1)


def farrest_in_tree(tree: list, current: int, visited: list, depth: int):
    visited[current] = True
    farrest, farrest_id = depth, current
    for neighbour in tree[current]:
        if not visited[neighbour]:
            tmp_farrest, tmp_farrest_id = farrest_in_tree(
                tree, neighbour, visited, depth + 1
            )
            if tmp_farrest > farrest:
                farrest, farrest_id = tmp_farrest, tmp_farrest_id
    return farrest, farrest_id


start = farrest_in_tree(tree, 0, [False] * n, 0)[1]
dist, end = farrest_in_tree(tree, start, [False] * n, 0)

# print(start + 1, end + 1)
print(dist)
