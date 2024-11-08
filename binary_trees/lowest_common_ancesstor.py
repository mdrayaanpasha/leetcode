# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode

        #STRATERGY:

        - so traverse thru node from root.
        - keep returning values as you traverse.
        - divide them into r and l.
        - if you have find one of p or q in the current node then in left subtree or right, return that tree thing and stop traversal there.
        - then traverse in the opp direction, if you find the other elem there good, else it means the first elem is the common ancesstor.
        - cause we were guaranteed to have both p & q.
        """
        
        if not root:
            return None

        if root == p or root == q:
            return root
        l=self.lowestCommonAncestor(root.left, p, q)
        r=self.lowestCommonAncestor(root.right,p,q)

        if l and r:
            return root
        else:
            return l or r
