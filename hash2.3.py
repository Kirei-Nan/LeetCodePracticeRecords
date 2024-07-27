class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record=[0]*26
        for c1 in s:
            record[ord(c1)-ord("a")]+=1
        for c2 in t:
            record[ord(c2) - ord("a")] -= 1
        for i in record:
            if i != 0:
                return False
        return True