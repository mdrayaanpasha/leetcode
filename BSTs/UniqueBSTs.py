# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[Optional[TreeNode]]


        EXPLAIN IT TO ME PHEEL????!@#!@#!

        - so its simply complicatedly englantly crafted peice of human neurons.

        so we recursively genereate all roots in trees, and then be like let me create all roots in the left and right also and then make it a tree and then add
        it in the result thing!

        """
        dp = {}

        def generate(left,right):
            if left > right:
                return [None]

            if (left,right) in dp:
                return dp[(left,right)]
            res=[]
            #these are all possible roots from left to rght.
            for val in range(left,right+1):
                #all possible left trees, left tree have stuff in this range: val > left and less then parent.val-1
                for leftTree in generate(left,val-1):
                    #all possible right trees, right trees have stuff in this range: val < parent.val and val>left
                    for rightTree in generate(val+1,right):
                        #creating trees out of these iteration meaning: for every roots every left trees, everyy right tree and then appenign it in the res.
                        root = TreeNode(val)
                        root.right=rightTree
                        root.left=leftTree
                        res.append(root)
                        dp[(left,right)]=res
            return res
        return generate(1,n) if n > 0 else []


