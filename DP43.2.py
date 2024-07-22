class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        if not nums1 or not nums2:
            return 0
        result=0
        dp=[[0]*len(nums1) for _ in range(len(nums2))]
        for i in range(len(nums1)):
            if nums2[0]==nums1[i]:
                dp[0][i] =1
                result=1
        for i in range(len(nums2)):
            if nums2[i]==nums1[0]:
                dp[i][0]=1
                result = 1

        for i in range(1,len(nums2)):
            for j in range(1,len(nums1)):
                if nums1[j] == nums2[i]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    result=max(result,dp[i][j])
        return result