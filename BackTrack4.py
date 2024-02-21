class Solution(object):
    def backtrack(self,n,k,startIndex,sum,path,result):
        if sum>n:
            return
        if len(path)==k:
            if sum==n:
                result.append(path[:])
            return
        for i in range(startIndex,9-(k-len(path))+2 ):
            path.append(i)
            sum+=i
            self.backtrack(n,k,i+1,sum,path,result)
            sum-=i
            path.pop()
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result=[]
        self.backtrack(n, k, 1, 0,[],result)
        return result
