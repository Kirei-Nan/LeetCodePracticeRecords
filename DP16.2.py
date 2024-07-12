class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if abs(target)>sum(nums):
            return 0
        if (target+sum(nums))%2==1:
            return 0
        aim=(sum(nums)-target)//2
        dp=[0]*(aim+1)
        dp[0]=1

        for i in range(len(nums)):
            for j in range(aim,nums[i]-1,-1):
                dp[j]+=dp[j-nums[i]]
        return dp[-1]