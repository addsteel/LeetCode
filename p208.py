class TrieNode:
    # Initialize your data structure here.
	def __init__(self):
		self.val = 0
		self.next = {}
class Trie:

	def __init__(self):
		self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
	def insert(self, word):
		length = len(word)
		node = self.root
		for c in word:
			if c in node.next:
				node = node.next[c]
			else:
				node.next[c] = TrieNode()
				node = node.next[c]
		node.val = 1
    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
	def search(self, word):
		node = self.root
		for c in word:
			if c in node.next:
				node = node.next[c]
			else:
				return False
		if node.val != 1:	return False
		return True

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
	def startsWith(self, prefix):
		node = self.root
		for c in prefix:
			if c in node.next:
				node = node.next[c]
			else:
				return False
		return True

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")