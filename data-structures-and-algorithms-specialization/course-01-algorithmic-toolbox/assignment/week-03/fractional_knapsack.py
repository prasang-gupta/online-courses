# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    best = [0] * len(weights)
    for i in range(len(weights)):
        best[i] = values[i] / weights[i]
    data = [(x, y, z) for x, y, z in sorted(zip(best, values, weights), reverse=True)]
    curweight = 0
    curidx = 0
    while curweight < capacity and curidx < len(data):
        if curweight + data[curidx][2] <= capacity:
            curweight += data[curidx][2]
            value += data[curidx][2] * data[curidx][0]
        else:
            adjustedweight = capacity - curweight
            curweight = capacity
            value += adjustedweight * data[curidx][0]
        curidx += 1
    return value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
