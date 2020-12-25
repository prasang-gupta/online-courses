#Uses python3

import sys

def isgreater(a, b):
    stra = str(a) + str(b)
    strb = str(b) + str(a)
    
    if int(stra) >= int(strb):
        return 1
    return 0

def largest_number(a):
    #write your code here
    res = ""
    while len(a):
        maxidx = 0
        maxval = a[0]
        for i in range(1, len(a)):
            if isgreater(a[i], maxval):
                maxval = a[i]
                maxidx = i
        a.pop(maxidx)
        res += str(maxval)
            
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
