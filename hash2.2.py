class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        result=[0]*26
        for i in s:
            result[ord(i)-ord("a")]+=1
        for i in t:
            result[ord(i) - ord("a")] -=1
        for i in range(26):
            if result[i]!=0:
                return False
        return True