class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        bits = [0 for i in xrange(0,32)]
        for num in nums:
            index = 0
            setBit = 1
            for i in xrange(0, 32):
                if num & setBit != 0:
                    bits[index] += 1
                index += 1
                setBit = setBit << 1
        print bits
        result = 0
        i = 30
        while i >= 0:
            if bits[i] % 3 == bits[31] % 3:
                result = result << 1
            else:
                result = (result << 1) + 1
                #print result
                #print i
            i -= 1
        if bits[31] % 3 != 0:
            return -result-1
        return result
nums = [1]
so = Solution()
print so.singleNumber(nums)