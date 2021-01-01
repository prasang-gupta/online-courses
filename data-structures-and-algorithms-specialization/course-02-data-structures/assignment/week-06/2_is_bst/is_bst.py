#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(2*10**9) # max depth of recursion
threading.stack_size(2**27)    # new thread will get stack of such size

class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        if self.n == 0:
            return True
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c
        return False

    def calcInOrder(self, node):
        if node == -1:
            return 0
        self.calcInOrder(self.left[node])
        self.result.append(self.key[node])
        self.calcInOrder(self.right[node])

    def IsBinarySearchTree(self):
        self.result = []
        self.calcInOrder(0)
        for i in range(len(self.result)-1):
            if self.result[i+1] < self.result[i]:
                return False
        return True

def main():
    tree = TreeOrders()
    if tree.read():
        print("CORRECT")
    else:
        if tree.IsBinarySearchTree():
            print("CORRECT")
        else:
            print("INCORRECT")

threading.Thread(target=main).start()
