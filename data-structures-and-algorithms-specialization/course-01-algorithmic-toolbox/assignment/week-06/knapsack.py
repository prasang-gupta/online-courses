# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    n = len(w)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n+1):
        for j in range(1, W+1):
            if j - w[i-1] >= 0:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i-1]] + w[i-1])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][W]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
