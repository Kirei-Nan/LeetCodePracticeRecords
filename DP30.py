class Solution:
    def robrange(self,nums,start,end):
        if start==end:
            return nums[start]

        dp=[0]*((end-start)+1)
        dp[0]=nums[start]
        dp[1]=max(nums[start],nums[start+1])

        for i in range(2,((end-start)+1)):
            dp[i] = max(dp[i - 1], dp[i - 1] + nums[i - 2])
        return dp[-1]
    def rob(self,nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums) == 1:
            return nums[0]

        result1=self.robrange(nums,0,len(nums)-2)
        result2=self.robrange(nums,1,len(nums)-1)
        return max(result1,result2)