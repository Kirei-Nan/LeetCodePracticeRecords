class Solution:
    def reverseWords(self, s: str) -> str:
        res=s.strip().split()
        left=0
        right=len(res)-1
        while left<right:
            res[left],res[right]=res[right],res[left]
            left+=1
            right-=1
        return ' '.join(res)