class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        prediff=0
        curdiff=0
        result=1
        for i in range(1,len(nums)):
            curdiff=nums[i]-nums[i-1]
            if prediff>=0 and curdiff<0 or prediff<=0 and curdiff>0:
                result+=1
                prediff=curdiff
        return result