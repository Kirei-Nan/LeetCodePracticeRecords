class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        record1=set()
        result=set()
        for i in nums1:
            record1.add(i)
        for i in nums2:
            if i in record1:
                result.add(i)
        return list(result)