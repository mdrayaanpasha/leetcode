class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
    

        def dfs(node):
            if not node:
                return 0
            left=dfs(node.left)
            right=dfs(node.right)


            return 1 + max(left,right)


        return dfs(root)