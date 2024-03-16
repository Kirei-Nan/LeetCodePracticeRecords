# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def traverse(self, left, right,nums):
        if left>right:
            return None
        mid=left+(right-left)//2
        root=TreeNode(nums[mid])
        root.left=self.traverse(left, mid-1,nums)
        root.right=self.traverse(mid+1,right, nums)
        return root
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        root=self.traverse(0, len(nums)-1,nums)
        return root

