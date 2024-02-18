# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.pre=None
        self.result=float('inf')
    def traverse(self, cur):
        if cur is None:
            return
        self.traverse(cur.left)
        if self.pre is not None:
            self.result=min(self.result, abs(self.pre.val-cur.val))

        self.pre=cur

        self.traverse(cur.right)

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.traverse(root)
        return self.result