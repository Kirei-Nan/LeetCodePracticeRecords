class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        n,m=len(haystack),len(needle)
        for i in range(n-m):
            for j in range(m):
                if haystack[i+j]!=needle[j]:
                    break
            else:
                return i
        return -1
