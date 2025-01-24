# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """

        SO HERE IS THE PLAN PHIIL!!!!

        - so why doint i sum it up and store that linked list in reverse order yea baby now we are talking arent we?
        - so traverse thru the node while you reverse it, well its weird that my mind thought i would reverse everything but now that
          am thinking i feel only reversing the last one would make more sense


        THAT STUFF MENTIONED ABOVE IS FUCKIN BULL SHIT!!!!!!!!

        so listen up you cranky old myself!!!!! you idiot you misunderstood the question it is all about carry operation not fuckin weid rotations and shit!!!!!

        """
        dummy = ListNode(1)
        curr = dummy
        carry = 0
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1+val2+carry
            carry = total // 10
            curr.next = ListNode(total%10)

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
            




