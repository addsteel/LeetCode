# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        length = 0
        tail = head
        while tail != None:
            tail = tail.next
            length += 1
        return self.sort(head, length)
    def sort(self, head, length):
        if head == None or head.next == None:
            return head
        tail = head
        for i in xrange(1, length/2):
            tail = tail.next
        head1 = tail.next
        tail.next = None
        head = self.sort(head, length/2)
        #print head.val
        head1 = self.sort(head1, length - length/2)
        #print head1.val
        return self.mergeList(head, head1)
    def mergeList(self, head1, head2):
        head = ListNode(0)
        tail = head
       # print head1.val
        #print head2.val
        while head1 != None and head2 != None:
            if head1.val > head2.val:
                tail.next = head2
                tail = tail.next
                head2 = head2.next
            else:
                tail.next = head1
                tail = tail.next
                head1 = head1.next
        if head1 != None:
            tail.next = head1
        if head2 != None:
            tail.next = head2
        tail = head.next
        while tail != None:
            print tail.val
            tail = tail.next
        print 
       # print head.next.val
        return head.next
n1 = ListNode(3)
n2 = ListNode(4)
n3 = ListNode(1)
n1.next = n2
n2.next = n3
so = Solution()
print so.sortList(n1).val
