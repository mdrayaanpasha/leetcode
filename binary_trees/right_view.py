# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        from collections import deque

        if not root:
            return []
        
        result=[]
        Q=deque([root])

        while Q:
            level_size=len(Q)

            for _ in range(level_size):
                node=Q.popleft()

                if _ == level_size - 1:
                    result.append(node.val)

                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)

        return result
