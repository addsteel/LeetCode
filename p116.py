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
        while root.left is not None:
            root.left.next = root.right
            nextNode = root.next
            pre= root.right
            while nextNode is not None:
                pre.next = nextNode.left
                nextNode.left.next = nextNode.right
                pre = nextNode.right
                nextNode = nextNode.next
            root = root.left
        return 