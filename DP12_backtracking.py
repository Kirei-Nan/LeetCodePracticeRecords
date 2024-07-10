class Solution:
    def getinput(self):
        n,capacity=map(int,input().split())
        weights=list(map(int,input().split()))
        values=list(map(int,input().split()))
        return n,capacity,weights,values

    def backtracking(self,n,capacity,weights,values,path,result,startIndex):
        if path>result:
            result=path

        for i in range(startIndex,n):
            if weights[i]<=capacity:
                path += values[i]
                capacity-=weights[i]
                self.backtracking(n,capacity,weights,values,path,result,i+1)
                capacity+=weights[i]
                path -= values[i]

solution=Solution()
n,capacity,weights,values=solution.getinput()
max=0
solution.backtracking(n,capacity,weights,values,0,max,0)
print(max)