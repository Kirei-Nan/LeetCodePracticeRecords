class Solution:
    def backtracking(self,n,k,result,path,startIndex):
        if len(path)==k:
            result.append(path[:])
            return

        for i in range(startIndex,n+1):
            path.append(i)
            self.backtracking(n, k, result, path, i+1)
            path.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:
        result=[]
        self.backtracking(n, k, result,[],1)
        return result