class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        total_sum=sum(nums)
        if target>total_sum:
            return 0
        if (total_sum+target)%2==1:
            return 0
        target_sum=(total_sum+target)//2
        dp=[0]*(target_sum+1)
        dp[0]=1
        for num in nums:
            for j in range(target_sum,num-1,-1):
                dp[j]+=dp[j-num]
        return dp[-1]
