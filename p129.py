# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:    return 0
        return self.recur(0, root)
    def recur(self, cur, node):
        cur = cur * 10 + node.val
        result = cur
        if node.left != None:
            result = self.recur(cur, node.left)
            if node.right != None:
                result += self.recur(cur, node.right)
        elif node.right != None:
            result = self.recur(cur, node.right)
        return result