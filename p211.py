class WordDictionary:
    # initialize your data structure here.
	def __init__(self):
		self.root = {}
    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
	def addWord(self, word):
		node = self.root
		for c in word:
			if c not in node:
				node[c] = {}
			node = node[c]
		node['#'] = {}
	# @param {string} word
	# @return {boolean}
	# Returns if the word is in the data structure. A word could
	# contain the dot character '.' to represent any one letter.
	def search(self, word, node = None):
		if node == None:
			node = self.root
		length = len(word)
		for i in xrange(0,length):
			if word[i] != '.':
				if word[i] in node:
					node = node[word[i]]
				else:
					return False
			else:
				if i+1 == length:
					for c in node:
						if '#' in node[c]:
							return True
					return False
				for c in node:
					if self.search(word[i+1:], node[c]) == True:	return True
				return False
		if '#' in node:	return True
		return False
# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")
wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("bad")
if wordDictionary.search(".ad"):	print "IN"