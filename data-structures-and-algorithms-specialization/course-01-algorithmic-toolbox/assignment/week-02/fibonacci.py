# Uses python3
def calc_fib(n):
    first = 0
    second = 1
    for _ in range(n):
        third = first + second
        first = second
        second = third
    return first

n = int(input())
print(calc_fib(n))