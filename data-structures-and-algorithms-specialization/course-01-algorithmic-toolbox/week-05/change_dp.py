# Uses python3
import sys

def get_change(m):
    #write your code here
    dp = [0] * (m + 1)
    for i in range(1, m+1):
        if i-4 >= 0:
            dp[i] = min(dp[i-1], dp[i-3], dp[i-4]) + 1
        elif i-3 >= 0:
            dp[i] = min(dp[i-1], dp[i-3]) + 1
        elif i-1 >= 0:
            dp[i] = dp[i-1] + 1
    return dp[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
