# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        if root.left is None and root.right is None:
            if root.val == sum: return True
            else:
                return False
        if root.left is not None:
            if self.hasPathSum(root.left, sum - root.val) is True:
                return True
        if root.right is not None:
            if self.hasPathSum(root.right, sum - root.val) is True:
                return True
        return False