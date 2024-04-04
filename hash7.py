class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        record=[0]*26
        for i in range(len(magazine)):
            record[ord(magazine[i])-ord('a')]+=1
        for i in range(len(ransomNote)):
            record[ord(ransomNote[i]) - ord('a')] -= 1
        for r in record:
            if r<0:
                return False
        return True