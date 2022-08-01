# Import
from math import inf

# Functions
def DFS(current: int, G: list, visited: list, path: list) -> None:
    """
    path: is a list of tuples (node, parent)

    What function do:
    - Mark all nodes that have path from current node to them"""
    visited[current] = True

    for neighbour in G[current]:
        if not visited[neighbour]:
            path.append((neighbour, path[-1][0]))
            DFS(neighbour, G, visited, path)


def find_loop(current: int, G: list, visited: list, path: list, loop: list):
    """
    path: is a list of tuples (node, parent)

    Return (loop, min_in_loop, min_in_loop_id)
    or -1 if there is no loop"""
    visited[current] = True

    for neighbour in G[current]:
        if not visited[neighbour]:
            path.append((neighbour, path[-1][0]))
            loop = find_loop(neighbour, G, visited, path, loop)
            if loop != -1:
                return loop
        else:
            neighbour_index = -1
            min_in_loop = inf
            min_in_loop_id = -1
            for i in range(len(path)):
                neighbour_id = path[i][0]
                if neighbour_index != -1:
                    if c[neighbour_id] < min_in_loop:
                        min_in_loop = c[neighbour_id]
                        min_in_loop_id = neighbour_id
                if neighbour_id == neighbour:
                    neighbour_index = i
                    min_in_loop = c[neighbour_id]
                    min_in_loop_id = neighbour_id

            loop = path[neighbour_index:]
            return loop, min_in_loop, min_in_loop_id
    return -1


# Variables
n, b, c, G1, G2 = None, None, None, None, None

# Get input
def get_input():
    global n, b, c, G1, G2
    n = int(input())
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    G1 = [[] for _ in range(n)]
    G2 = [[] for _ in range(n)]

    for u in range(n):
        v = b[u] - 1
        G1[u].append(v)
        G2[v].append(u)


# Main
if __name__ == "__main__":
    get_input()

    visited = [False] * n
    bombs = []
    cost = 0

    for i in range(n):
        if not visited[i]:
            # path = BFS(i, G2, visited)
            # bombs.append(path[-1])
            tmp_visited = [False] * n
            loop, min_in_loop, min_in_loop_id = find_loop(
                i, G1, tmp_visited, [(i, -1)], []
            )
            cost += min_in_loop
            bombs.append(min_in_loop_id + 1)
            DFS(min_in_loop_id, G2, visited, [(min_in_loop_id, -1)])
            # print(loop)

    # print(bombs)
    print(cost)
