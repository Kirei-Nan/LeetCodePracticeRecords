class Solution:
    def backtracking(self,path,result,startIndex,n,k):
        if len(path)==k:
            result.append(path[:])
        for i in range(startIndex,n+1):
            path.append(i)
            self.backtracking(path,result,i+1,n,k)
            path.pop()
    def combine(self, n: int, k: int) -> List[List[int]]:
        result=[]
        self.backtracking([],result,1,n,k)
        return result
