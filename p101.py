# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:  return True
        return self.isTreesSymmetric(root.left, root.right)
    def isTreesSymmetric(self, tree1, tree2):
        if tree1 is None and tree2 is None:
            return True
        if tree1 is not None and tree2 is not None:
            if tree1.val == tree2.val:
                return self.isTreesSymmetric(tree1.right, tree2.left) and self.isTreesSymmetric(tree1.left, tree2.right)
        return False