# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:	return True
        dep,result = self.depth(root)
        return result
    def depth(self, root):
        if root is None:    return 0, True
        leftDep, leftSign = self.depth(root.left)
        rightDep, rightSign = self.depth(root.right)
        if leftSign and rightSign and abs(rightDep - leftDep) < 2:
            return max(rightDep, leftDep)+1, True
        else:
            return 0, False