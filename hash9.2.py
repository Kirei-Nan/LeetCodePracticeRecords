class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result=[]

        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                left=j+1
                right=len(nums)-1
                while left<right:
                    if nums[i]+nums[j]+nums[left]+nums[right]>target:
                        right-=1
                    elif nums[i]+nums[j]+nums[left]+nums[right]<target:
                        left+=1
                    else:
                        result.append([nums[i],nums[j],nums[left],nums[right]])
                        while right>left and nums[left]==nums[left+1]:
                            left+=1
                        while right>left and nums[right]==nums[right-1]:
                            right-=1
                        right -= 1
                        left += 1
        return result