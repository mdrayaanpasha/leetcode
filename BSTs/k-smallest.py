# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count=0
        result=None


        def traverse(node):
            nonlocal count,result
            if not node:
                return
            if node.left:
                traverse(node.left)
            count+=1
            if(count == k):
                result=node.val
                return 
            if node.right:
                traverse(node.right)


        traverse(root)

        return result
