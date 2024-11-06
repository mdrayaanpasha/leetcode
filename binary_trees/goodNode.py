class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def helper(node, max_so_far, counter):
            if node:
                if node.val >= max_so_far:
                    counter[0]+=1
                    max_so_far=node.val
                
                helper(node.left,max_so_far,counter)
                helper(node.right,max_so_far,counter)


        c = [0]
        helper(root, root.val, c)

        return c[0]
