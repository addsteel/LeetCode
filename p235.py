# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
	def __init__(self):
		self.stack = []
		self.shareStack = []
	def lowestCommonAncestor(self, root, p, q):
		if p == None or q == None:
			return None
		self.p = p
		self.q = q
		return self.firOrderTraversal(root)
	def firOrderTraversal(self, node):
		p = self.p
		q = self.q
		self.stack.append(node)
		if node == p or node == q:
			if self.shareStack == []:
				for i in xrange(0, len(self.stack)):
					self.shareStack.append(self.stack[i])
			else:
				minLen = len(self.stack)
				if minLen > len(self.shareStack):
					minLen = len(self.shareStack)
				print minLen
				shareLen = 0
				while shareLen < minLen and self.stack[shareLen] == self.shareStack[shareLen]:
					shareLen += 1
				return self.stack[shareLen-1]
		if node.left != None:
			t = self.firOrderTraversal(node.left)
			if t != None:
				return t
		if node.right != None:
			t = self.firOrderTraversal(node.right)
			if t != None:
				return t
		self.stack.pop()
		return None
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t1.left = t2
t1.right = t3
so = Solution()
print so.lowestCommonAncestor(t1, t1, t3).val