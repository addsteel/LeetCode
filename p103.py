# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:    return []
        stack = [root]
        result = []
        sign = True
        level = 0
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
            if level % 2 == 1:
                result.append(tmpResult[::-1])
            else:
                result.append(tmpResult)
            level += 1
            stack = nextStack
        return result