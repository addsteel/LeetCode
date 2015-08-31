# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        cur = root
        result = []
        while cur != None:
            if cur.left == None:
                result.append(cur.val)
                cur = cur.right
                continue
            preCur = cur.left
            #find preNode
            while preCur.right != None and preCur.right != cur:
                preCur = preCur.right
            if preCur.right == cur:
                cur = cur.right
                preCur.right = None
            else:
                result.append(cur.val)
                preCur.right = cur
                cur = cur.left
        return result
l = [1,2]
r = [3,4]
print [0] + l + r