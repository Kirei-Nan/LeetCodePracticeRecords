class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 !=0:
            return False
        target=sum(nums)//2
        dp=[0]*(target+1)

        for i in range(len(nums)):
            for j in range(target,nums[i]-1,-1):
                dp[j]=max(dp[j],dp[j-nums[i]]+nums[i])
        return dp[-1]==target