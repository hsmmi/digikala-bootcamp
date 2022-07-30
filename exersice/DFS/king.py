n = int(input())

per = tuple(map(int, input().split()))
goal = tuple(range(1, n + 1))


def neighbors(per):
    return [per[:i+1][::-1] + per[i+1:] for i in range(1, len(per))]


mark = {}


def BFS(per):
    mark[per] = True
    queue = [(per, 0)]
    while queue:
        per, dist = queue.pop(0)
        if per == goal:
            return dist
        for nper in neighbors(per):
            if nper not in mark:
                mark[nper] = True
                queue.append((nper, dist + 1))

    return -1


print(BFS(per))
