# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minNode(self,root):
        temp=root

        while temp.left:
            temp=temp.left

        return temp.val


    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """

        if root == None:
            return root
        
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)

        else:
            #now there can be some cases like there is one child or there is 2 child 
            #if there is one child:

            if root.right == None:
                return root.left
            
            if root.left == None:
                return root.right

            
            #if it came here then it means it has 2 children.
            #statergy is to get the min value of right node. and then delete 
            # that value from there. and then kinda like place that value in the 
            # prev root we left!

            minVal = self.minNode(root.right)
            root.val=minVal
            root.right=self.deleteNode(root.right, minVal)

        return root
        