class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp=[False]*(len(s)+1)
        dp[0]=True

        for j in range(1,len(s)+1):
            for word in wordDict:
                if j>=len(word):
                    dp[j]=dp[j] or (dp[j-len(word)] and s[j-len(word):j] in wordDict)
        return dp[-1]