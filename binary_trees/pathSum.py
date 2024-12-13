# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.sum=self.val

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
     if not root:
        return False
     
     stk=[(root,root.val)]

     while stk:
        node,curr_sum = stk.pop()

        if curr_sum == targetSum and not node.left and not node.right:
            return True

        if node.left:
            stk.append((node.left,curr_sum+node.left.val))

        if node.right:
            stk.append((node.right,curr_sum+node.right.val))


     return False

