# python3

def siftdown(data, idx, swap):
    size = len(data)
    minval = data[idx]
    if (2 * idx) + 1 < size and minval > data[(2 * idx) + 1]:
        minval = data[(2 * idx) + 1]
        minchild = (2 * idx) + 1
    if (2 * idx) + 2 < size and minval > data[(2 * idx) + 2]:
        minval = data[(2 * idx) + 1]
        minchild = (2 * idx) + 2
    if minval == data[idx]:
        return 0
    temp = data[minchild]
    data[minchild] = data[idx]
    data[idx] = temp
    swap.append([idx, minchild])
    siftdown(data, minchild, swap)

def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    size = len(data)
    depth = 2
    while (size // depth) != 0:
        depth = depth * 2
    if depth == 2:
        return swaps
    start = int((depth/2) - 2)

    for i in range(start, -1, -1):
        tempswap = []
        siftdown(data, i, tempswap)
        for obj in tempswap:
            swaps.append(obj)

    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
