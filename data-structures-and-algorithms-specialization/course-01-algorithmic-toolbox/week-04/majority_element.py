# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    mid = left + ((right - left) // 2)
    first = get_majority_element(a, left, mid)
    second = get_majority_element(a, mid, right)

    if first == second:
        return first

    count_first = 0
    count_second = 0
    for i in range(left, right):
        if a[i] == first:
            count_first += 1
        if a[i] == second:
            count_second += 1
    if count_first > ((right - left) // 2):
        return first
    if count_second > ((right - left) // 2):
        return second
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
