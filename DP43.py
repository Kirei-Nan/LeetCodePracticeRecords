class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp=[[0]*len(nums1) for _ in range(len(nums2))]
        result=0
        for i in range(len(nums1)):
            if nums1[i]==nums2[0]:
                dp[i][0]=1
        for j in range(len(nums2)):
            if nums1[0]==nums2[j]:
                dp[0][j]=1

        for i in range(1,len(nums1)):
            for j in range(1,len(nums2)):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    result=max(result,dp[i][j])
        for row in dp:
            print(row)
        return result
