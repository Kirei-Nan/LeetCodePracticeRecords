class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum=0
        result=-float('inf')
        for i in range(len(nums)):
            cursum+=nums[i]
            if cursum>result:
                result=cursum
            if cursum<0:
                cursum=0
        return result

