class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
	def rotate(self, nums, k):
		if len(nums) <= 1:	return nums
		k = k % len(nums)
		nums[0:-k] = self.reverse(nums[0:-k])
		#self.reverse(nums[0:-k])
		#print nums
		nums[-k:] = self.reverse(nums[-k:])
		#self.reverse(nums[-k:])
		#print nums
		#nums = self.reverse(nums)
		self.reverse(nums)
		return
	def reverse(self, nums):
		halfLength = len(nums)/2
		for i in xrange(0,halfLength):
			nums[i],nums[-i-1] = nums[-i-1],nums[i]
		return nums
so = Solution()
nums = [1,2,3,4,5,6,7]
so.rotate(nums,3)
print nums