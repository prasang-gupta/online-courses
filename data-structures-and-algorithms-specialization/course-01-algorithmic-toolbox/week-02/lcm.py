# Uses python3
import sys

def lcm_naive(a, b):
    mult = a * b
    while b:
        rem = a % b
        a = b
        b = rem

    return int(mult / a)

if __name__ == '__main__':
    #input = sys.stdin.read()
    a, b = map(int, input().split())
    print(lcm_naive(a, b))

