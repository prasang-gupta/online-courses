# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)    # new thread will get stack of such size

class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def calcInOrder(self, node):
        if node == -1:
            return 0
        self.calcInOrder(self.left[node])
        self.result.append(self.key[node])
        self.calcInOrder(self.right[node])

    def calcPreOrder(self, node):
        if node == -1:
            return 0
        self.result.append(self.key[node])
        self.calcPreOrder(self.left[node])
        self.calcPreOrder(self.right[node])

    def calcPostOrder(self, node):
        if node == -1:
            return 0
        self.calcPostOrder(self.left[node])
        self.calcPostOrder(self.right[node])
        self.result.append(self.key[node])

    def inOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        self.calcInOrder(0)
        return self.result

    def preOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        self.calcPreOrder(0)                 
        return self.result

    def postOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        self.calcPostOrder(0)            
        return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
