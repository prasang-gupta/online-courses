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

    def find(self, node, k):
        if node == -1:
            return False
        if self.key[node] == k:
            return True
        elif self.key[node] > k:
            if self.left[node] != -1:
                return self.find(self.left[node], k)
            return False
        else:
            if self.right[node] != -1:
                return self.find(self.right[node], k)
            return False
            
    def calcInOrder(self, node):
        if node == -1:
            return 0

        self.calcInOrder(self.left[node])

        if self.prevkey == 'first':
            self.prevkey = self.key[node]
        else:
            if self.key[node] < self.prevkey:
                self.flag = False
            if self.key[node] == self.prevkey:
                if self.find(self.left[node], self.prevkey):
                    self.flag = False
            self.prevkey = self.key[node]

        self.calcInOrder(self.right[node])

    def IsBinarySearchTree(self):
        self.flag = True
        self.prevkey = "first"
        self.calcInOrder(0)
        return self.flag

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
