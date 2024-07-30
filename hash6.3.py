class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        record={}
        result=0
        for i in nums1:
            for j in nums2:
                record[i+j]=record.get(i+j,0)+1
        for i in nums3:
            for j in nums4:
                target=-i-j
                if target in record:
                    result+=record[target]
        return result