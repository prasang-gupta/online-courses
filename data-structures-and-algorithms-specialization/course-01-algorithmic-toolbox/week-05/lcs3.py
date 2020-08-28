#Uses python3

import sys

def lcs3(a, b, c):
    #write your code here
    la = len(a)
    lb = len(b)
    lc = len(c)

    dp = [[[0 for _ in range(lc + 1)] for _ in range(lb + 1)] for _ in range(la + 1)]
    
    for i in range(1, la+1):
        for j in range(1, lb+1):
            for k in range(1, lc+1):
                if a[i-1] == b[j-1] == c[k-1]:
                    dp[i][j][k] = dp[i-1][j-1][k-1] + 1
                else:
                    dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])
    
    return dp[la][lb][lc]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
