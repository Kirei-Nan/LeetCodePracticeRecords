# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 1:
            return TreeNode(nums[0])
        max_val=0
        max_index=0
        if nums:
            max_val=max(nums)
            max_index = nums.index(max_val)
            root = TreeNode(max_val)
            root.left = self.constructMaximumBinaryTree(nums[:max_index])
            root.right = self.constructMaximumBinaryTree(nums[max_index + 1:])
            return root