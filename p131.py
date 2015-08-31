class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        length = len(s)
        if length < 2:
            if length == 0: 
                return []
            else:
                return [[s]]
        length = len(s)
        pos = length - 1
        lists = {}
        while pos >= 0:
            self.add(s, lists, pos)
            pos -= 1
        return lists[0]
    def add(self, s, lists, pos):
        if pos >= len(s) - 1:
            if pos == len(s) - 1:
                lists[pos] = [[s[-1:]]]
            return
        index = pos
        length = len(s)
        lists[pos] = []
        bound = (length + pos) / 2 + 1
        while index < bound:
            rpos = index
            while rpos < length - 1 and s[rpos] == s[rpos+1]:
                rpos += 1
            lpos = index
            while lpos > pos and s[lpos] == s[lpos-1]:
                lpos -= 1
            if lpos == pos:
                rpos += 2
                p = lpos + 1
                while p < rpos:
                    if p in lists:
                        for l in lists[p]:
                            lists[pos].append([s[pos:p]] + l)
                    else:
                        lists[pos].append([s[pos:]])
                    p += 1
                index = rpos - 1
                continue
            lpos -= 1
            rpos += 1
            index = rpos
            while lpos >= pos and rpos < length and s[lpos] == s[rpos]:
                lpos -= 1
                rpos += 1
            if lpos < pos:
                if rpos in lists:
                    t = [s[pos:rpos]]
                    for l in lists[rpos]:
                        lists[pos].append(t+l)
                elif rpos == length:
                    lists[pos].append([s[pos:rpos]])
                else:
                    print pos, rpos
so = Solution()
s = "abbab"
print so.partition(s)