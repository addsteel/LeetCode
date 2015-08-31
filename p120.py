class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 0:
            return 0
        if len(triangle) == 1:
            return triangle[0][0]
        sums = [num for num in triangle[-1]]
        length = len(triangle)
        for j in xrange(1, length):
            index = - j - 1
            tmp = [0 for num in triangle[index]]
            for i in xrange(0, len(triangle[index])):
                tmp[i] = triangle[index][i] + sums[i]
                if sums[i] > sums[i+1]:
                    tmp[i] = triangle[index][i] + sums[i+1]
            sums = tmp
        return sums[0]