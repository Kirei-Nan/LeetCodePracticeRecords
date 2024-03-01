class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result=float('-inf')
        sum=0
        for i in nums:
            sum+=i
            if sum>=result:
                result=sum
            if sum<0:
                sum=0
        return result