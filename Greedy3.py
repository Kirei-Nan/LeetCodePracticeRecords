class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return len(nums)

        prediff=nums[1]-nums[0]
        count=2 if prediff!=0 else 1
        for i in range(2,len(nums)):
            diff=nums[i]-nums[i-1]
            if (diff>0 and prediff<=0) or (diff<0 and prediff>=0):
                count+=1
                prediff=diff
        return count