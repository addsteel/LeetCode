# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None
class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
	def removeNthFromEnd(self, head, n):
		if n == 0: return head
		front_pnt = head
		for i in xrange(0,n+1):
			if front_pnt != None:
				front_pnt = front_pnt.next
			else:
				head = head.next
				return head
		behind_pnt = head
		while front_pnt != None:
			front_pnt = front_pnt.next
			behind_pnt = behind_pnt.next
		behind_pnt.next = behind_pnt.next.next
		return head