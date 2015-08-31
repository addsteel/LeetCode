# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root is None:    return []
        #leaf node
        #print root.val, sum
        if root.left is None and root.right is None:
            #print 'Fine'
            #print root.val, sum
            if root.val == sum:
                #print 'Fine'
                return [[root.val]]
            else:   return []
        result = []
        #print root.val, sum
        left = self.pathSum(root.left, sum - root.val)
        for path in left:
            result.append([root.val] + path)
        #print left
        right = self.pathSum(root.right, sum - root.val)
        for path in right:
            result.append([root.val] + path)
        #print right
        return result
root = TreeNode(7)
right1 = TreeNode(2)
left10 = TreeNode(3)
right11 = TreeNode(-7)
root.right = right1
right1.left = left10
right1.right = right11
so = Solution()
print so.pathSum(root,2)
