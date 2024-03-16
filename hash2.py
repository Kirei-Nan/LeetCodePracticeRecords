class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count=[0 for _ in range(26)]
        for i in s:
            count[ord(i)-ord('a')]+=1
        for i in t:
            count[ord(i)-ord('a')]-=1
        for i in count:
            if i !=0:
                return False
        return True