# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    allseq = [0]
    dp = [1] * (n+1)
    for i in range(1, n+1):
        div3 = div2 = minus1 = -1
        if i % 3 == 0:
            div3 = dp[i//3] + 1
        if i % 2 == 0:
            div2 = dp[i//2] + 1
        minus1 = dp[i-1] + 1

        if div3 != -1 and div2 != -1:
            if div3 <= div2 and div3 <= minus1:
                allseq.append(i//3)
                dp[i] = dp[i//3] + 1
            elif div2 <= div3 and div2 <= minus1:
                allseq.append(i//2)
                dp[i] = dp[i//2] + 1
            else:
                allseq.append(i-1)
                dp[i] = dp[i-1] + 1
        elif div3 != -1:
            if div3 <= minus1:
                allseq.append(i//3)
                dp[i] = dp[i//3] + 1
            else:
                allseq.append(i-1)
                dp[i] = dp[i-1] + 1
        elif div2 != -1:
            if div2 <= minus1:
                allseq.append(i//2)
                dp[i] = dp[i//2] + 1
            else:
                allseq.append(i-1)
                dp[i] = dp[i-1] + 1
        else:
            allseq.append(i-1)
            dp[i] = dp[i-1] + 1
    
    cur = n
    while cur != 0:
        sequence.append(cur)
        cur = allseq[cur]
    
    return reversed(sequence)


input = sys.stdin.read()
n = int(input)
# n = 96234
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
