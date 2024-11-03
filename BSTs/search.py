# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """

        temp=root

        while temp:
            if temp.val > val:
                temp=temp.left
            elif temp.val < val:
                temp=temp.right
            else:
                return temp

        