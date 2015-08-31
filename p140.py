class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = {}
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        size = len(s)
        dp = [False] * size
        for i in range(size):
            for j in range(i+1, size+1):
                if s[i:j] not in wordDict:
                    continue
                if i == 0 or (i > 0 and dp[i-1]):
                    dp[j-1] = True
        if dp[size - 1] == False:   return []
        result = []
        if len(s) == 0: return result
        dictTree = Node(0)
        for word in wordDict:
            node = dictTree
            for chr in word:
                if chr not in node.next:
                    node.next[chr] = Node(0)
                node = node.next[chr]
            node.val = 1
        curString = ""
        self.search(dictTree, s, result, curString)
        return result
    def search(self, dictTree, s, result, curString):
        """
        :type s: str
        :type dictTree: Set[None]
        :rtype: bool
        """
        if len(s) == 0: return
        node = dictTree
        for i,c in enumerate(s):
            if c in node.next:
                node = node.next[c]
                if node.val == 1:
                    #print s[i+1:]
                    self.search(dictTree, s[i+1:], result, curString + s[0:i+1] + " ")
            else:
                return
        if node.val == 1:
            result.append(curString + s)