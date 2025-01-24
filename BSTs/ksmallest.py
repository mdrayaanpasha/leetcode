class Solution(object):
    def kthSmallest(self, root, k):
        keys = []

        def inorderTraverse(node):
            if node:
                inorderTraverse(node.left)
                if len(keys) < k:
                    keys.append(node.val)
                inorderTraverse(node.right)

        inorderTraverse(root)
        return keys[k-1]
