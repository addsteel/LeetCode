class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        strs = filter(None, s.split(' '))
        length = len(strs)
        result = ""
        for i in xrange(1, length+1):
            result += strs[-i] + " "
        return result[0:-1]
s = "      a           a"
so = Solution()
print so.reverseWords(s)