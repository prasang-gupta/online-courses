#Uses python3

import sys

def lcs2(a, b):
    #write your code here
    la = len(a)
    lb = len(b)

    dp = [[0 for _ in range(lb + 1)] for _ in range(la + 1)]
    
    for i in range(1, la+1):
        for j in range(1, lb+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[la][lb]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    # a = [2,7,5]
    # b = [2,5]

    print(lcs2(a, b))
