class Solution(object):
    def backtrack(self,n,k,startIndex,path,result):
        if len(path)==k:
            result.append(path[:])
            return result
        for i in range(startIndex,n-(k-len(path))+2):
            path.append(i)
            self.backtrack(n,k,i+1,path,result)
            path.pop()


    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result=[]
        self.backtrack(n, k, 1, [],result)
        return result

