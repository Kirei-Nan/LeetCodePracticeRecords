class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1:
            return True
        i=0
        cover=0

        while i<=cover:
            cover=max(cover,i+nums[i])
            if cover>=len(nums)-1:
                return True
            i+=1
        return False