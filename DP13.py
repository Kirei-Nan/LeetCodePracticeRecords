class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        totalsum=sum(nums)
        if totalsum % 2!=0:
            return False
        target=totalsum//2
        dp=[False for i in range(target+1)]
        dp[0]=True
        for num in nums:
            for i in range(target,num-1,-1):
                dp[i]=dp[i] or dp[i-num]
        return dp[target]