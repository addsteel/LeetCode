# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head == None:    return
        node = head
        length = 0
        while node != None:
            node = node.next
            length += 1
        if length <= 2: return 
        midLength = length/2
        node = head
        for i in xrange(0, midLength-1):
            node = node.next
        #print node.val
        head2 = node.next
        node.next = None
        head2 = self.reverse(head2)
        #print head2.val
        head1 = head
        head = ListNode(0)
        tail = head
        while head1 != None:
            #print head1.val
            tail.next = head1
            head1 = head1.next
            tail.next.next = head2
            tail = head2
            head2 = head2.next
        if head2 != None:
            tail.next = head2
            tail = tail.next
        tail.next = None
        head = head.next
    def reverse(self, node):
        if node == None or node.next == None:
            return node
        pre = node
        mid = node.next
        node.next = None
        while mid != None:
            behind = mid.next
            mid.next = pre
            pre = mid
            mid = behind
        return pre
so = Solution()
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n1.next = n2
n2.next = n3
so.reorderList(n1)
while n1 != None:
    print n1.val
    n1 = n1.next