# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None
class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
		size = 0
		node = head
		while node != None:
			size += 1
			node = node.next
		#if size == 0: return False
		if size <= 1: return True
		halfSize = size/2
		node = head
		for i in xrange(1,halfSize):
			node = node.next
		leftNode = node
		rightNode = leftNode.next
		if size % 2 == 1:
			rightNode = rightNode.next
		#print leftNode.val
		#print rightNode.val
		#break the list
		leftNode.next = None
		#reverse the left part of list
		first = head
		second = head.next
		while second != None:
			third = second.next
			second.next = first
			first = second
			second = third
		for i in xrange(1, halfSize+1):
			print leftNode.val
			print rightNode.val
			if leftNode.val == rightNode.val:
				leftNode = leftNode.next
				rightNode = rightNode.next
			else:
				return False
		return True
head = ListNode(0)
tail = ListNode(1)
head.next = tail
tail = ListNode(0)
head.next.next = tail
so = Solution()
if so.isPalindrome(head):
	print 'Palindrome'