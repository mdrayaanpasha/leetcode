# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]


        so if it were bst, boy it would have been interesting....

        so it now, here is the stratergy tho

        - how about we traverse normally thru the thing.
        first elem is the root, and if you take inorder then elems before that num are to left of
        the tree and others to the right.


        """

        if not inorder or not preorder:
            return None

        root_value = preorder.pop(0)
        root = TreeNode(root_value)

        index_root_inorder=inorder.index(root_value)

        root.left=self.buildTree(preorder,inorder[:index_root_inorder])
        root.right=self.buildTree(preorder,inorder[index_root_inorder+1:])


        return root
        
