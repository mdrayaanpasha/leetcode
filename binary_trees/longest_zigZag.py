# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.Max=0

        def helper(node,isRight,D):
            if not node: return

            self.Max=max(self.Max,D)
            if isRight:
                helper(node.left,False,D+1)
                helper(node.right,True,1)
            else:
                helper(node.right,True,D+1)
                helper(node.left,False,1)

            
        helper(root,True,0)
        helper(root,False,0)

        return self.Max