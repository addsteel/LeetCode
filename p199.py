# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def __init__(self):
		self.result = []
	# @param {TreeNode} root
	# @return {integer[]}
	def rightSideView(self, root):
		self.result = []
		if root != None:
			self.preOrderTraversal(root,1)
		return self.result
	def preOrderTraversal(self, root, depth):
		if depth > len(result):
			self.result.append(root.val)
		if root.right != None:
			self.preOrderTraversal(root.right, depth+1)
		if root.left != None:
			self.preOrderTraversal(root.left,depth+1)