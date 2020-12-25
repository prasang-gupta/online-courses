# Uses python3
import sys

def gcd_naive(a, b):
    while b:
        rem = a % b
        a = b
        b = rem

    return a

if __name__ == "__main__":
    #input = sys.stdin.read()
    a, b = map(int, input().split())
    print(gcd_naive(a, b))
