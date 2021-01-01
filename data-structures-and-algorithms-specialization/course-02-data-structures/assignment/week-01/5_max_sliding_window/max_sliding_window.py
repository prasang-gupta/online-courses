# python3

from collections import deque

def max_sliding_window_naive(sequence, m):
    maximum = []
    q = deque()
    
    for i in range(m):
        while q and sequence[i] >= sequence[q[-1]]:
            q.pop()
        q.append(i)
    
    for i in range(m, len(sequence)):
        maximum.append(sequence[q[0]])
        while q and q[0] <= i - m:
            q.popleft()
        while q and sequence[i] >= sequence[q[-1]]:
            q.pop()
        q.append(i)
    
    maximum.append(sequence[q[0]])
    return maximum

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))

