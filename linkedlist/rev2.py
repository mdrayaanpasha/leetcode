# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
-Stratergy is simple:

+ go till left node. reverese till right.
+ make left point to right.next and prev of left to right.

"""
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head


        dummy=ListNode(0,head)

        LeftPrev,curr=dummy,head

        #lets take this pointer to a postion that can help us ya know reverse from left.
        for _ in range(left-1):
            LeftPrev,curr=curr,curr.next


        #now think bout it, so u gotta like do it from l to r, so r-l+1 cause see it on a paper it will make sense.
        prev=None
        for _ in range(right-left+1):
            #here just gonna rev it!
            Next=curr.next
            curr.next=prev
            prev=curr
            curr=Next

        #now ill be having a reversed thing, but pointers are fucked up!!
        # so lets point that left to right.next, so right.next is actaully curr
        # and prev is like right.
        
        LeftPrev.next.next=curr
        LeftPrev.next=prev

        return dummy.next
        
        
