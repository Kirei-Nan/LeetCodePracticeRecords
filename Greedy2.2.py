class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        count=0
        j=0
        for i in g:
            while j<len(s):
                if s[j]>=i:
                    count+=1
                    j += 1
                    break;
                j+=1
        return count