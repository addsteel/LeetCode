class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result = result ^ num
        i = 0
        while i < 32:
            if ((result >> i ) & 1) != 0:
                break
            i += 1
        num1 = 0
        for num in nums:
            if ((num >> i) & 1) != 0:
                num1 = num1 ^ num
        return [num1, result ^ num1]