# Uses python3
import sys

inf = sys.maxsize

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def MinAndMax(i, j, operators, M, m):
    if i == j:
        return m[i][j], M[i][j]
    minval = inf
    maxval = -inf
    for k in range(i,j):
        a = evalt(M[i][k], M[k+1][j], operators[k])
        b = evalt(M[i][k], m[k+1][j], operators[k])
        c = evalt(m[i][k], M[k+1][j], operators[k])
        d = evalt(m[i][k], m[k+1][j], operators[k])
        minval = min(minval, a, b, c, d)
        maxval = max(maxval, a, b, c, d)
    return minval, maxval

def get_maximum_value(dataset):
    #write your code here
    digits = [0] * (len(dataset) // 2 + 1)
    operators = [0] * (len(digits) - 1)
    for i in range(len(dataset)):
        if i % 2 == 0:
            digits[i//2] = dataset[i]
        else:
            operators[i//2] = dataset[i]

    n = len(digits)
    M = [[0 for _ in range(n)] for _ in range(n)]
    m = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        M[i][i] = int(digits[i])
        m[i][i] = int(digits[i])
    for s in range(n):
        for i in range(n-s):
            j = i + s
            m[i][j], M[i][j] = MinAndMax(i, j, operators, M, m)
    
    return M[0][n-1]

if __name__ == "__main__":
    print(get_maximum_value(input()))