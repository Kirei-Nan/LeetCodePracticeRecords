class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        dp=[1]*len(nums)
        result=0
        for i in range(len(nums)):
            if nums[i]>nums[i-1]:
                dp[i]=dp[i-1]+1
            result=max(result,dp[i])
        return result
