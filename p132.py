class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length < 2:
            return 0
        result = {}
        result[length] = -1
        for i in xrange(0, length):
            result[i] = length
        pos = length - 1
        while pos >= 0:
            self.subMinCut(s, pos, result)
            print result[pos]
            pos -= 1
        return result[0]
    def subMinCut(self, s, pos, result):
        length = len(s)
        if pos == length - 1:
            result[pos] = 0
            return
        index = pos
        bound = (length + pos) / 2 + 1
        while index < bound:
            rpos = index
            while rpos < length - 1 and s[rpos] == s[rpos+1]:
                rpos += 1
            lpos = index
            while lpos > pos and s[lpos] == s[lpos-1]:
                lpos -= 1
            rpos += 1
            lpos -= 1
            #Some Trick
            index = rpos
            if lpos < pos:
                result[pos] = result[pos+1] +1
                for i in xrange(pos+1, rpos+1):
                    if result[pos] > 1 + result[i]:
                        result[pos] = 1 + result[i]
                continue
            while lpos >= pos and rpos < length and s[lpos] == s[rpos]:
                lpos -= 1
                rpos += 1
            if lpos < pos:
                if result[rpos] + 1 < result[pos]:
                    result[pos] = result[rpos] + 1