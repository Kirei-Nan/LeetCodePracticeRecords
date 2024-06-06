class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp=[0]*(len(nums))
        result=0

        for i in range(len(nums)):
            dp[i]=max(dp[i-1]+nums[i],nums[i])
            if dp[i]>result:
                result=dp[i]
        return result
