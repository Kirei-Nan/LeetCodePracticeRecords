class Solution:
    def sortedSquares(self,nums):
        result=[float('inf')]*len(nums)
        left=0
        right=len(nums)-1
        i=len(nums)-1
        while left<=right:
            if nums[left]**2>nums[right]**2:
                result[i]=nums[left]**2
                i-=1
                left+=1
            else:
                result[i]=nums[right]**2
                i-=1
                right-=1
        return result