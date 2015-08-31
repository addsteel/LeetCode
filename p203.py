# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
	def removeElements(self, head, val):
		prev = ListNode(0)
		prev.next = head
		cur = head
		head = prev
		while cur != None:
			if cur.val == val:
				prev.next = cur.next
				cur = cur.next
			else:
				prev = cur
				cur = cur.next
		return head.next