class Solution:
	# @param {TreeNode} root
	# @return {TreeNode}
	def invertTree(self, root):
		if root == None:
			return None
		if root.left == None and root.right == None:
			return root
		p = root.left
		root.left = self.invertTree(root.right)
		root.right = self.invertTree(p)
		return root