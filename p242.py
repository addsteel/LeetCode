class Solution:
	# @param {string} s
	# @param {string} t
	# @return {boolean}
	def isAnagram(self, s, t):
		hash = {}
		for c in s:
			if c in hash:
				hash[c] += 1
			else:
				hash[c] = 1
		for c in t:
			if c in hash:
				hash[c] -= 1
			else:
				return False
		for c in hash:
			if hash[c] != 0:
				return False
		return True