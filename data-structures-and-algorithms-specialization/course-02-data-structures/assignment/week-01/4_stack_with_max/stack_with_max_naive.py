#python3
import sys

class StackWithMax():
    def __init__(self):
        self.stack = []
        self.maxstack = []

    def Push(self, a):
        self.stack.append(a)
        if len(self.maxstack) == 0:
            self.maxstack.append(a)
        else:
            self.maxstack.append(max(a, self.maxstack[-1]))

    def Pop(self):
        assert(len(self.stack))
        self.stack.pop()
        self.maxstack.pop()

    def Max(self):
        assert(len(self.stack))
        return self.maxstack[-1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
