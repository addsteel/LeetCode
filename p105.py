# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.inorder = None
        self.preorder = None
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) < 2:
            if len(inorder) == 0:
                return None
            else:
                return TreeNode(inorder[0])
        self.inorder = inorder
        self.preorder = preorder
        return self.buildTreeInplace(0, len(preorder), 0 , len(preorder))
    def buildTreeInplace(self, prebegin, preend, inbegin, inend):
        length = inend - inbegin
        if length < 2:
            if length == 0: return None
            else:   return TreeNode(self.inorder[inbegin])
        inorder = self.inorder
        preorder = self.preorder
        for i in xrange(inbegin, inend):
            if inorder[i] == preorder[prebegin]:
                root = TreeNode(inorder[i])
                root.left = self.buildTreeInplace(prebegin + 1, prebegin + 1 + i - inbegin, inbegin, i)
                root.right = self.buildTreeInplace(prebegin + 1 + i- inbegin, preend, i+1, inend)
                return root
        return None