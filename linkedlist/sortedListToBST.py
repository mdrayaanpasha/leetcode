# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]

        WHATS THE PLAN PHIEEEELLLL!@#!@#!??

        - what if everytime we keep on moving to the mid value.
        - give that node as the current node value and give list before mid for left.
           - this would be: start:mid -> head:mid
        - after it for right.
           - this would be: mid+1:end -> mid:null!!


        HOW TO SOLVE???!@#!@#

        - go to mid using s,f pointers.
        - once in the mid, then augment stuff and send it.   
        """


        while fast and fast.next:
            fast = fast.next.next
            slow=slow.next
        
