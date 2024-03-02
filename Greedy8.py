class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return 0
        index=0
        count=0
        while index<len(nums)-1:
            max=0
            for i in range(nums[index]+1):
                if index + i < len(nums) and index+nums[index+i]>max:
                    max=index+nums[index+i]
            index=max
            count+=1
        return count