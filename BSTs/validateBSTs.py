# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool


        WHATS THE PLAN PHEEEL?????

        - see about every BST, it is valid, given if it is within the range and so are its 
          childrens.
        - so root get inf range first then.
        - right must be within (node.val,Max) -> saying you cant be less then your parent b****
        - left must be withing (Min,node.val) -> saying you cant be more then your parent b****
        """
        def Valid(node,Min,Max):
            if not node:
                return True
            
            if node.val >= Max or node.val <= Min:
                return False
                
            if node.left and not Valid(node.left,Min,node.val):
                return False
            if node.right and not Valid(node.right,node.val,Max):
                return False
            
            return True

        return Valid(root,float('-inf'),float('inf'))
        
