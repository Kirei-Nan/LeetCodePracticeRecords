class Solution:
    def backtracking(self,s: str, wordDict: List[str],startIndex:int):
        if startIndex>=len(s):
            return True
        for i in range(startIndex,len(s)):
            if s[startIndex:i+1] in wordDict and self.backtracking(s,wordDict,i+1):
                return True
        return False
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.backtracking(s, wordSet, 0)