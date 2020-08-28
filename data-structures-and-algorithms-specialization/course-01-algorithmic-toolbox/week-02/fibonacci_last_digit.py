# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    first = 0
    second = 1
    for _ in range(n):
        third = (first + second) % 10
        first = second
        second = third
    return first % 10

if __name__ == '__main__':
    #input = sys.stdin.read()
    n = int(input())
    print(get_fibonacci_last_digit_naive(n))
