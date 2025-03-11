# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]

        so whats the plan pheel???/

        - we move 3 steps eveytime. and be like swap 2 elems. given it has an elem adjacent to it.
        """

        dummy = ListNode(-1)
        dummy.next=head
        prev=dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = first.next
            
            first.next=second.next
            second.next=first
            
            
            prev.next=second
            prev=first
        
        return dummy.next
