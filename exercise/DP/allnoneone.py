# Import


# Functions


# Variables


# Get input
from operator import index


def get_input():
    global n, s, c, min_box, sum_box

    n, s = map(int, input().split())

    c = []
    min_box = []
    sum_box = []

    for _ in range(n):
        box = list(map(int, input().split()))[1:]
        min_element = min(box)
        min_box.append(min_element)
        sum_element = sum(box)
        sum_box.append(sum_element)

        c.append(box)
    pass


def noneoneall(min_element: int, sum_element: int, price: int):
    """
    get box min element and sum of the box and the price
    return the cost that we can get with none, one, all of the box"""
    none = 0
    one = -1
    all = -1
    if min_element <= price:
        one = min_element
    if sum_element <= price:
        all = sum_element

    return none, one, all


def max_val_index(val: list) -> list:
    """
    get values
    return max value and it's index"""
    max_val, max_index = val[0], 0
    for i in range(1, len(val)):
        if val[i] > max_val:
            max_val, max_index = val[i], i

    return max_val, max_index


def size_cost(box: list, index: int) -> int:
    """
    get a box and cost index
    return the size of the box with index"""
    if index == 0:
        return 0
    if index == 1:
        return 1

    return len(box)


def solve():
    global n, s, c
    # cp[i][j]: maximum item to get with first i box with money j
    cp = [[0 for _ in range(s + 1)] for _ in range(n)]
    # sp[i][j]: how to get here
    sp = [["" for _ in range(s + 1)] for _ in range(n)]

    for price in range(1, s + 1):
        # initial value
        # Get from first box
        costs = noneoneall(min_box[0], sum_box[0], price)
        cost, index = max_val_index(costs)
        size_element = size_cost(c[0], index)
        cp[0][price] = size_element
        sp[0][price] = str(index)

        # fill dp
        for box in range(1, n):
            costs = noneoneall(min_box[box], sum_box[box], price)

            tmp_cp = []
            tmp_cp.append(cp[box - 1][price])
            tmp_cp.append(
                -1 if costs[1] == -1 else cp[box - 1][price - min_box[box]] + 1
            )
            tmp_cp.append(
                -1
                if costs[2] == -1
                else cp[box - 1][price - sum_box[box]] + len(c[box])
            )

            cost, index = max_val_index(tmp_cp)
            size_element = size_cost(c[box], index)
            cp[box][price] = cp[box - 1][price - costs[index]] + size_element
            sp[box][price] = sp[box - 1][price - costs[index]] + str(index)

    return cp[n - 1][s], sp[n - 1][s]


# Main
if __name__ == "__main__":
    get_input()
    len_item, path = solve()
    print(len_item)
    print(path)
    pass
