class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        record={}
        result=0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]+nums2[j] in record:
                    record[nums1[i]+nums2[j]]+=1
                else:
                    record[nums1[i] + nums2[j]]=1
        for i in range(len(nums3)):
            for j in range(len(nums4)):
                if -nums3[i]-nums4[j] in record:
                    result+=record[nums3[i]+nums4[j]]
        return result