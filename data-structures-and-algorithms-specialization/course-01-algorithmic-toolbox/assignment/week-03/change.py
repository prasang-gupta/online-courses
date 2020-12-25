# Uses python3
import sys

def get_change(m):
    #write your code here
    no10 = m // 10
    m -= no10 * 10

    no5 = m // 5
    m -= no5 * 5

    no1 = m

    return no10 + no5 + no1

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
