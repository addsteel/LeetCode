# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = []
        node = root
        while node != None:
            self.stack.append(node)
            node = node.left

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.stack != []

    # @return an integer, the next smallest number
    def next(self):
        if self.stack != []:
            node = self.stack.pop()
        else:
            return 0
        result = node.val
        if node.right != None:
            node = node.right
            while node != None:
                self.stack.append(node)
                node = node.left
        return result

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t2.left = t1
t2.right = t3
so = BSTIterator(t2)
i = 10
while so.hasNext() and i > 0:
    print so.next()
    i -= 1
# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())