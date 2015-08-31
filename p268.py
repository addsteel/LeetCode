class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        for num in nums:
            sum += num
        n = len(nums)
        return n * (n - 1) / 2 - sum