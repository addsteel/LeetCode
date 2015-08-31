class Solution:
	# @param {integer} s
	# @param {integer[]} nums
	# @return {integer}
	def minSubArrayLen(self, s, nums):
		length = len(nums)
		if length == 0:
			return 0
		if s == 0:	return 0
		leftPos = 0
		rightPos = 1
		curSum = nums[0]
		minGap = length+1
		while rightPos < length:
			while rightPos < length and curSum < s:
				curSum += nums[rightPos]
				rightPos += 1
			if curSum < s:	break
			while leftPos < rightPos and curSum >= s:
				curSum -= nums[leftPos]
				leftPos += 1
			if rightPos - leftPos + 1 < minGap:	minGap = rightPos - leftPos + 1
			if minGap == 1:	return 1
		if minGap == length + 1:	return 0
		else:	return minGap