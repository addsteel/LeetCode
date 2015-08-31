class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement(self, nums):
        if len(nums) == 0:  return -1
        if len(nums) == 1 or nums[0] > nums[1]:  return 0
        if nums[-1] > nums[-2]:   return len(nums) - 1
        for i in xrange(1, len(nums)-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i
        return -1