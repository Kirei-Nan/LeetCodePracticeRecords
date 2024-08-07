class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result=float('-inf')
        for i in range(1,len(prices)):
            result+=max(prices[i]-prices[i-1],0)
        return result
