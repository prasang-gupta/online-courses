# Uses python3
import sys
import math

def optimal_summands(n):
    summands = []
    #write your code here
    num = math.floor((math.sqrt(8*n + 1) - 1) / 2)
    summands = list(range(1, num))
    sum = int(((num-1) * num) / 2)
    summands.append(n - sum)
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
