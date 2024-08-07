class Solution:
    def reverse(self,s):
        left=0
        right=len(s)-1
        while left<right:
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
        return s
    def reverseStr(self, s: str, k: int) -> str:
        res=list(s)
        for cur in range(0,len(s),2*k):
            res[cur:cur+k]=self.reverse(res[cur:cur+k])
        return ''.join(res)