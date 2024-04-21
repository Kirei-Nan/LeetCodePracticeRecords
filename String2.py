class Solution:
    def reverse(self,text):
        left=0
        right=len(text)-1
        while left<right:
            text[left],text[right]=text[right],text[left]
            left+=1
            right-=1
        return text

    def reverseStr(self, s: str, k: int) -> str:
        if len(s)<k:
            return s

        res=list(s)
        for i in range(0,len(s),2*k):
            res[i:i+k]=self.reverse(res[i:i+k])
        return ''.join(res)
