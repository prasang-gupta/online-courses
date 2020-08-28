# Uses python3
def edit_distance(s, t):
    #write your code here
    a = s
    b = t
    s = len(a)
    t = len(b)

    dp = [[0 for _ in range(t + 1)] for _ in range(s + 1)]
    dp[0] = [i for i in range(t + 1)]
    for i in range(s + 1):
        dp[i][0] = i
    
    for i in range(1, s + 1):
        for j in range(1, t + 1):
            if a[i-1] == b[j-1]:
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1])
            else:
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)
    
    return dp[s][t]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
