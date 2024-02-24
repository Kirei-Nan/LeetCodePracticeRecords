class Solution(object):
    def isPalindrome(self,string,left,right):
        while left < right:
            if string[left] != string[right]:
                return False
            left+=1
            right-=1
        return True

    def backtrack(self, s,path,result,startIndex):
        if startIndex==len(s):
            result.append(path[:])
            return
        for i in range(startIndex,len(s)):
            if self.isPalindrome(s,startIndex,i):
                path.append(s[startIndex:i+1])
                self.backtrack(s,path,result,i+1)
                path.pop()
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result=[]
        self.backtrack(s,[],result,0)
        return result