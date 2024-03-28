class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        totalsum=sum(stones)
        target=totalsum//2
        dp=[0]*(target+1)
        for i in range(len(stones)):
            for j in range(target,stones[i]-1,-1):
                dp[j]=max(dp[j],dp[j-stones[i]]+stones[i])
        larger=totalsum-dp[-1]
        smaller=dp[-1]
        return larger-smaller