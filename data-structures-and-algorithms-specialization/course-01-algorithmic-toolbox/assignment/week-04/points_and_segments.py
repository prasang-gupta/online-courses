# Uses python3
import sys

def binary_search_right(a, x):
    left, right = 0, len(a) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if a[mid] > x:
            right = mid - 1
        else:
            left = mid + 1
    return left, mid, right

def binary_search_left(a, x):
    left, right = 0, len(a) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return left, mid, right

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    #write your code here
    starts.sort()
    ends.sort()
    s = len(starts)

    for idx in range(len(points)):
        p = points[idx]
        l, m, r = binary_search_right(starts, p)
        if l > m:
            onright = s - l
        else:
            onright = s - m

        l, m, r = binary_search_left(ends, p)
        if l > m:
            onleft = l
        else:
            onleft = r + 1
            
        cnt[idx] = s - onleft - onright

    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
