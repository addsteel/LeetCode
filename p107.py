# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:	return []
        stack = [root]
        result = []
        sign = True
        while sign:
            sign = False
            nextStack = []
            tmpResult = []
            for node in stack:
                if node.left is not None:
                    nextStack.append(node.left)
                    sign = True
                if node.right is not None:
                    nextStack.append(node.right)
                    sign = True
            tmpResult.append(node.val)
            result.append(tmpResult)
            stack = nextStack
        return result[::-1]
