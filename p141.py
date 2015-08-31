# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        node1 = head
        count = 1
        while node1 != None:
            count += 1
            node1 = node1.next
            if count > 1000:    break
        if node1 == None:   return False
        node2 = node1
        while node2 != None:
            for i in xrange(0,10):
                node2 = node2.next
                if node2 == None:
                    return False
                if node2 == node1:
                    return True
            node1 = node1.next
        return False