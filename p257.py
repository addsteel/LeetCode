# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        result = []
        if root == None:    return result
        path = ""
        self.reverse(root,path,result)
        return result
    def reverse(self, node, path, result):
        if node.left == None and node.right == None:
            result.append(path + "%d" %node.val)
        else:
            if node.left != None:
                self.reverse(node.left, path + "%d->" %node.val, result)
            if node.right != None:
                self.reverse(node.right, path + "%d->" %node.val, result)
        return 
tn = TreeNode(1)
tn1 = TreeNode(2)
tn2 = TreeNode(3)
tn.left = tn1
tn.right = tn2
so = Solution()
print so.binaryTreePaths(tn)
