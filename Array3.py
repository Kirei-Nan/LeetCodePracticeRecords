class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[left]=nums[i]
                left+=1
        return left