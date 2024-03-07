class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        hash=[0]*27
        for i in range(len(s)):
            hash[ord(s[i])-ord('a')]=i
        result=[]
        right=0
        left=0
        for i in range(len(s)):
            right=max(right,hash[ord(s[i])-ord('a')])
            if i==right:
                result.append(right-left+1)
                left=right+1
        return result