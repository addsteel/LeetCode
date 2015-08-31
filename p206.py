# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
	def reverseList(self, head):
		if head == None or head.next == None:	return head
		behind = head
		mid = head.next
		front = mid.next
		head.next = None
		while front != None:
			mid.next = behind
			behind = mid
			mid = front
			front = front.next
		mid.next = behind
		return mid