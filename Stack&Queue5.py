class Solution:
    def removeDuplicates(self, s: str) -> str:
        res=[]
        for i in range(len(s)):
            if len(res)==0 or s[i]!=res[-1]:
                res.append(s[i])
            else:
                res.pop()
        return "".join(res)