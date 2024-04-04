class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        record={}
        for n1 in nums1:
            for n2 in nums2:
                record[n1+n2]=record.get(n1+n2,0)+1
        count=0
        for n3 in nums3:
            for n4 in nums4:
                key=-n3-n4
                if key in record:
                    count+=record[key]
        return count