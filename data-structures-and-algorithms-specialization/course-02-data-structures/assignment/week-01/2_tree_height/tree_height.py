# python3

import sys
import threading

class Node:
    def __init__(self, data):
        self.child = []
        self.data = data
    
    def addchild(self, childnode):
        self.child.append(childnode)

def compute_height(n, parents):
    # Replace this code with a faster implementation
    nodes = [0] * n
    for i in range(n):
        nodes[i] = Node(i)
    
    for i in range(n):
        parent = parents[i]
        if parent == -1:
            root = nodes[i]
        else:
            nodes[parent].addchild(nodes[i])

    queue = [root]
    depthcount = 0

    while len(queue) != 0:
        newq = []
        for i in range(len(queue)):
            for childnode in queue[i].child:
                newq.append(childnode)
        queue = newq
        depthcount += 1

    return depthcount


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
