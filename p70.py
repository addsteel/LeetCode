class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        result = [1,1]
        while len(result) < n
            result.append(result[-1]+result[-2])
        return result[-1]