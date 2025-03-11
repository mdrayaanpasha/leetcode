# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]

        so whats the plan pheel???

        - so how about firs we take the len of the nodes L, L - n we wanna go and stop.
        - then prev->next = curr->next
        """

        L = 0
        temp=head
        while temp:
            L+=1
            temp=temp.next

        K = L - n

        if K == 0:
            return head.next
        temp=head
        for i in range(K-1):
            temp=temp.next

        temp.next=temp.next.next

        return head

        


        
