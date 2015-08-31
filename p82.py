# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	# @param {ListNode} head
	# @return {ListNode}
	def deleteDuplicates(self, head):
		if head == None:	return head
		node = ListNode(head.val+1)
		node.next = head
		head = node
		while node.next != None and node.next.next != None:
			if node.next.next.val != node.next.val:	node = node.next
			else:
				val = node.next.val
				mv_node = node.next.next.next
				while mv_node != None and mv_node.val == val:
					mv_node = mv_node.next
				node.next = mv_node
		return head.next