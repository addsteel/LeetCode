# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root == None:    return
        self.myFlatten(root)
        return
    def myFlatten(self ,root):
        right = root.right
        leftEnd = root
        if root.left != None:
            leftEnd = self.myFlatten(root.left)
            root.right = root.left
            root.left = None
        if right != None:
            rightEnd = self.myFlatten(right)
            leftEnd.right = right
            leftEnd = rightEnd
        return leftEnd