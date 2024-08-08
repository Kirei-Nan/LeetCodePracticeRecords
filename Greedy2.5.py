class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        s_index=0
        g_index=0
        result=0
        while s_index<len(s) and g_index<len(g):
            if s[s_index]>=g[g_index]:
                result+=1
                s_index+=1
                g_index+=1
            else:
                s_index+=1
        return result