class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        startx=starty=0
        count=1
        result=[[0]*n for _ in range(n)]
        mid=n//2


        for offset in range(n//2):
            for i in range(starty,n-offset-1):
                result[startx][i] =count
                count+=1
            for i in range(startx,n-offset-1):
                result[i][n-offset-1]=count
                count+=1
            for i in range(n-offset-1,starty,-1):
                result[n-offset-1][i]=count
                count+=1
            for i in range(n-offset-1,startx,-1):
                result[i][starty]=count
                count += 1
            startx+=1
            starty+=1
        if n%2!=0:
            result[mid][mid]=count
        return result
