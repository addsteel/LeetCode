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
    # @param two ListNodes
    # @return the intersected ListNode
	def getIntersectionNode(self, headA, headB):
		if headA == headB:	return headA
		pntA = headA
		pntB = headB
		lenBC = 0
		while pntB != None:
			lenBC += 1
			pntB = pntB.next
		lenAC = 0
		while pntA != None:
			lenAC += 1
			pntA = pntA.next
		headA = self.reverseList(headA)
		pntB = headB
		lenBA = 0
		while pntB != None:
			lenBA += 1
			pntB = pntB.next
		#Attention
		lenC = (lenAC + lenBC - lenBA + 1)/2
		pntC = headA
		headA = self.reverseList(headA)
		lenA = lenAC - lenC
		lenB = lenBC - lenC
		if lenA < 0 or lenB < 0:
			return None
		pntA = headA
		pntB = headB
		for i in xrange(0, lenA):
			pntA = pntA.next
		for i in xrange(0, lenB):
			pntB = pntB.next
		if pntA == pntB:
			return pntA
		else:
			return None
		return None
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
class Solution1:
    # @param two ListNodes
    # @return the intersected ListNode
	def getIntersectionNode(self, headA, headB):
		if headA == None or headB == None:
			return None
		pntA = headA
		pntB = headB
		signA = True
		signB = True
		while pntA != pntB:
			pntA = pntA.next
			if pntA == None:
				if signA == True:
					pntA = headB
					signA = False
				else:
					return None
			pntB = pntB.next
			if pntB == None:
				if signB == True:
					pntB = headA
					signB = False
				else:
					return None
		return pntA
pntA = ListNode(1)
#pntB = None
pntB = ListNode(2)
pntA.next = pntB 
so = Solution1()
pntC = so.getIntersectionNode(pntA, pntB)
if pntC != None:	print pntC.val