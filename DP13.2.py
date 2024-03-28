class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        totalsum=sum(nums)
        if totalsum%2==1:
            return False

        target=totalsum/2

        dp=[0]*(target+1)
        for i in range(len(nums)):
            for j in range(target,nums[i]-1,-1):
                dp[j]=max(dp[j],dp[j-nums[i]]+nums[i])
        print(dp)
        if dp[-1]==target:
            return True
        return False