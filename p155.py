class MinStack:
    # initialize your data structure here.
    def __init__(self):
        self.stack = []
        self.minStack = []
    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.stack.append(x)
        if self.minStack == [] or self.minStack[-1] >= x:
            self.minStack.append(x)
    # @return nothing
    def pop(self):
        if self.stack[-1] == self.minStack[-1]:
            self.minStack.pop()
        self.stack.pop()
    # @return an integer
    def top(self):
        return self.stack[-1]
    # @return an integer
    def getMin(self):
        return self.minStack[-1]