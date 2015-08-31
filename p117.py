# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if root is None:
            return
        while root is not None:
            while root != None and root.left is None and root.right is None:
                root = root.next
            if root == None:    return
            if root.left != None:
                root.left.next = root.right
            pre = root.left
            if root.right != None:
                pre = root.right
            nextNode = root.next
            while nextNode != None:
                if nextNode.left != None:
                    nextNode.left.next = nextNode.right
                    pre.next = nextNode.left
                    pre = nextNode.left
                    if nextNode.right != None:
                        pre = nextNode.right
                elif nextNode.right != None:
                    pre.next = nextNode.right
                    pre = nextNode.right
                nextNode = nextNode.next
            if root.left != None:
                root = root.left
            else:
                root = root.right
        return 