class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        result=0
        for i in range(len(s)):
            if result<len(g) and s[i]>=g[result]:
                result+=1
        return result