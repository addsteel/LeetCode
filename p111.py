# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        minRes = 1000000000
        if root.left is not None:
            minRes = self.minDepth(root.left)
        if root.right is not None:
            minRes = min(minRes,self.minDepth(root.right))
        return minRes + 1