# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.res = 0
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:    return 0
        self.res = root.val
        self.getMaxPath(root)
        return self.res
    def getMaxPath(self, root):
        if root is None:
            return 0
        maxLeftResult = max(0,self.getMaxPath(root.left))
        maxRightResult = max(0, self.getMaxPath(root.right))
        self.res = max(self.res, root.val + maxLeftResult + maxRightResult)
        return root.val + max(maxLeftResult, maxRightResult)