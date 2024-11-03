# Definition for a binary tree node.

from collections import deque
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root == None:
            return 0

        Q=deque()
        Q.append(root)
        current_level=1
        max_level=1
        max_sum=float('-inf')


        while Q:
            s=0
            for _ in range(len(Q)):
                elem=Q.popleft()
                if elem.right:
                    Q.append(elem.right)
                if elem.left:
                    Q.append(elem.left)
                s+=elem.val

            if s > max_sum:
                max_sum=s
                max_level=current_level
            
            current_level+=1

        return max_level