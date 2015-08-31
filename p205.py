class Solution:
    # @param {string} s
    # @param {string} t
	# @return {boolean}
	def isIsomorphic(self, s, t):
		length = len(s)
		if length != len(t):	return False
		if length == 0:	return True
		sMapt = {}
		tMaps = {}
		for i in xrange(0,length):
			if s[i] in sMapt:
				if sMapt[s[i]] != t[i]:	return False
			elif t[i] not in tMaps:
				sMapt[s[i]] = t[i]
				tMaps[t[i]] = s[i]
			else:
				return False
		return True