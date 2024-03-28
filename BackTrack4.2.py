class Solution:
    def backtracking(self,k,n,result,path,startIndex,sum):
        if len(path)==k:
            if sum==n:
                result.append(path[:])
            return
        for i in range(startIndex,10):
            sum+=i
            path.append(i)
            self.backtracking(k,n,result,path,i+1,sum)
            sum-=i
            path.pop()
    def combinationSum3(self, k, n):
        result=[]
        self.backtracking(k,n,result,[],1,0)
        return result