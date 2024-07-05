class Solution:
    def isPalindrome(self,s:str,left:int,right:int)->bool:
        if len(s)==0:
            return
        while left<right:
            if s[left] != s[right]:
                return False
            left+=1
            right-=1
        return True
    def backtracking(self,s:str,path:List[str],result:List[List[str]],startIndex:int)->None:
        if startIndex>=len(s):
            result.append(path[:])
            return
        for i in range(startIndex,len(s)):
            if not self.isPalindrome(s,startIndex,i):
                continue
            path.append(s[startIndex:i+1])
            self.backtracking(s,path,result,i+1)
            path.pop()


    def partition(self, s: str) -> List[List[str]]:
        result=[]
        self.backtracking(s,[],result,0)
        return result