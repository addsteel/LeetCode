# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        try:
            fast = head.next
            slow = head
            while fast is not slow:
                fast = fast.next.next
                slow = slow.next
        except:
            return None
        slow = slow.next
        while head != slow:
            head = head.next
            slow = slow.next
        return head
n1 = ListNode(1)
n1.next = n1
so = Solution()
if so.detectCycle(n1) != None:
    print so.detectCycle(n1).val