# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
==============================STRATERGY==================================

- lets maitain prev & curr, prev being previous and curr being current.

- create Ans linkedList, & Have a pointer AnsHead pointing to its head.
- then traverse thru the linked list, and only do Ans.next=curr if prev.data != curr.data and curr.next.data != curr.data given they both exist.

- then return AnsHead

====================================================================="""
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy=ListNode(0)
        Ans=dummy

        prev=None
        curr=head

        while curr:
            if (prev is None or prev.val!=curr.val) and (curr.next is None or curr.next.val!=curr.val):
                Ans.next=curr
                Ans=Ans.next
            prev=curr
            curr=curr.next

        
        Ans.next=None


        return dummy.next

        
