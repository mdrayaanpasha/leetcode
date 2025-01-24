# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]

        whats the plan phil???

        - first find the lenght of linked list - N
        - then perform mod operation to know how many rotations needed - R
        - point NH to node after N-R entries.
        - then iterate R times, where:
          - temp = NH
            NH.next = Head
            Head=NH
            NH = temp.next

        """
        if not head or k == 0:
            return head

        
        temp = head
        n=0
        while temp:
            n+=1
            temp=temp.next

        k%= n
        if k == 0:
            return head
        
        new_tail_pos = n-k-1

        temp=head
        for _ in range(n-k-1):
            temp=temp.next

        newHead = temp.next
        temp.next=None


        old_tail = newHead

        while old_tail.next:
            old_tail=old_tail.next

        old_tail.next=head

        return newHead
