# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.pre=None
        self.maxcount=float('-inf')
        self.count=0
        self.result=[]
    def traverse(self, cur):
        if not cur:
            return
        self.traverse(cur.left)
        if self.pre is None:
            self.count=1
        elif self.pre.val==cur.val:
            self.count+=1
        elif self.pre.val != cur.val:
            self.count=1

        self.pre=cur

        if self.count>self.maxcount:
            self.maxcount=self.count
            self.result=[cur.val]
        elif self.count==self.maxcount:
            self.result.append(cur.val)
        self.traverse(cur.right)

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.traverse(root)
        return self.result