class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        def string_cmp(left,right):
            if left + right < right + left:
                return 1
            elif left + right > right + left:
                return -1
            return 0
        strings = []
        sign = False
        for n in nums:
            if n != 0:  sign = True
            strings.append(str(n))
        if sign == False:   return "0"
        strings = sorted(strings, cmp = string_cmp)
        result = ""
        for s in strings:
            result += s
        return result