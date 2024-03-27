class Solution:
    def combine(self,n,k):
        result=[]
        self.backtracking([],result,n,k,1)
        return result
    def backtracking(self,path,result,n,k,startIndex):
        if len(path)==k:
            result.append(path[:])
            return
        for i in range(startIndex,n+1):
            path.append(i)
            self.backtracking(path,result,n,k,i+1)
            path.pop()