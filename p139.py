class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = {}
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        #return True
        if len(s) == 0: return True
        wordList = []
        for word in wordDict:
            #print word
            wordList.append(word)
        wordList.sort(key = len)
        dictTree = Node(0)
        for word in wordList:
            if self.search(dictTree, word) == True: continue
            #print word
            node = dictTree
            for chr in word:
                if chr not in node.next:
                    node.next[chr] = Node(0)
                node = node.next[chr]
            node.val = 1
        return self.search(dictTree, s)
    def search(self, dictTree, s):
        """
        :type s: str
        :type dictTree: Set[None]
        :rtype: bool
        """
        if len(s) == 0: return True
        node = dictTree
        for i,c in enumerate(s):
            if c in node.next:
                node = node.next[c]
                if node.val == 1:
                    #print s[i+1:]
                    if self.search(dictTree, s[i+1:]) == True:
                        return True
            else:
                return False
        if node.val == 1:
            return True
        return False
so = Solution()
s = "aaaaaaa"
wordDict = {"aa"}
if so.wordBreak(s, wordDict):
    print "11111111"