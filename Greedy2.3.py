class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        result=0
        j=0
        for i in range(len(s)):
            if j<len(g) and s[i] >= g[j]:
                result += 1
                j+=1

        return result

