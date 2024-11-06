# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        from collections import defaultdict
        self.dict=defaultdict(int)
        self.dict[0]=1
        self.total=0
        def DFS(node,PS):
            if node:
                CS=node.val+PS
                self.total+=self.dict.get(CS-targetSum,0)
                self.dict[CS]+=1

                DFS(node.left,CS)
                DFS(node.right,CS)
                self.dict[CS]-=1

        DFS(root,0)

        return self.total
