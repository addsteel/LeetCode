class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        if numRows == 0:
            return result
        result.append([1])
        for i in xrange(1, numRows):
            tmp = [1]
            for i in xrange(0, len(result[-1])-1):
                tmp.append(result[-1][i] + result[-1][i+1])
            tmp.append(1)
            result.append(tmp)
        return result
        getRow