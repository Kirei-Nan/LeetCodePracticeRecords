class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result=set()
        set1=set(nums1)
        for i in nums2:
            if i in set1:
                result.add(i)
        return list(result)
