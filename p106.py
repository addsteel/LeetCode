# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.inorder = None
        self.postorder = None
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) < 2:
            if len(inorder) == 0:   return None
            else:
                return TreeNode(inorder[0])
        self.inorder = inorder
        self.postorder = postorder
        return self.buildTreeInplace(0, len(inorder), 0 , len(postorder))
    def buildTreeInplace(self, inbegin, inend, postbegin, postend):
        length = inend - inbegin
        if length < 2:
            if length == 0: return None
            else:   return TreeNode(self.inorder[inbegin])
        inorder = self.inorder
        postorder = self.postorder
        for i in xrange(inbegin, inend):
            if inorder[i] == postorder[postend-1]:
                root = TreeNode(inorder[i])
                root.left = self.buildTreeInplace(inbegin, i, postbegin, postbegin + i - inbegin)
                root.right = self.buildTreeInplace(i+1, inend, postbegin + i - inbegin, postend-1)
                return root
        return None