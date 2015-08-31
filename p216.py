class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
	def combinationSum3(self, k, n):
		result = []
		path = []
		if n > 45 or k > 9:	return []
		self.getCombination(k, n, 1, result, path)
		return result
	def getCombination(self, k, n, depth, result, path):
		if k < 1 or k + depth > 10 or 2 * n > (depth + 9) * (9 - depth + 1) or 2 * n > (9 + 9 + 1 - k) * k:	return
		if k == 1:
			if n <= 9 and n >= depth:
				result.append(path + [n])
			return
		self.getCombination(k, n, depth+1, result, path)
		self.getCombination(k-1, n-depth, depth+1, result, path + [depth])
		return