# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        # my stratergy is to like kinda first go the mid and then reverse it!
        # then add them and see which is max and return.

        #lets find mid:
        slow=fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        #assuming that i have my mid in slow, i wanna reverse my linkedlist from there

        prev=None
        curr=slow
        Next=None

        while curr:
            Next=curr.next
            curr.next=prev
            prev=curr
            curr=Next


        #now i have my first node in head, and from mid in prev.
        m=0

        while prev:
            if head.val + prev.val > m:
                m= head.val + prev.val
            head=head.next
            prev=prev.next

        
        return m