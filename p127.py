class Solution(object):
    def ladderLength(self, beginWord, endWord, wordDict):
        """
        :type beginWord: str
        :type endWord: str
        :type wordDict: Set[str]
        :rtype: int
        """
        if beginWord not in wordDict or endWord not in wordDict:
            return 0
        wordD.remove(beginWord)
        dict = {}
        length = len(beginWord)
        for i in xrange(0, length+1):
            dict[i] = set()
        beginWordSet = set([beginWord])
        while True:
            for word1 in wordDict:
                dif = self.wordCmp(word1, beginWord)
                dict[dif].add(word1)
            
            if self.wordCmp(beginWord, endWord) != length:
                searchSet = set()
                for i in xrange(1, self.wordCmp(beginWord, endWord)+1):
                    searchSet = searchSet | dict[i]
                depth = self.cur(beginWordSet, endWord, searchSet)
                return depth
            else:
                depth1 = self.cur(beginWordSet, dict[length])
                return self.cur(dict[length-1], endWord, dict[length])
    def cur(self, beginWordSet, endWord, wordDict):
        for word in beginWordSet:
            if self.wordCmp(word, endWord) <= 2:
                return self.wordCmp(word, endWord)+1
        nextSet = set()
        for word1 in beginWordSet:
            for word2 in wordDict:
                if self.wordCmp(word1, word2) <= 2:
                    nextSet.add(word2)
        if len(nextSet) == 0:   return 0
        for word in nextSet:
            wordDict.remove(word)
        depth = self.cur(nextSet, endWord, wordDict)
        if depth == 0:
            return 0
        return 1+depth
    def wordCmp(self, word1, word2):
        result = 0
        for i in xrange(0, len(word1)):
            if word1[i] != word2[i]:
                result += 1
        return result