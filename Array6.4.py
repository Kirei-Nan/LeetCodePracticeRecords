class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result=[[0]*n for _ in range(n)]
        startx=0
        starty=0
        offset=1
        count=1
        mid=n//2

        while offset<=n//2:
            for i in range(starty, n - offset):
                result[startx][i] =count
                count+=1
            for i in range(startx,n-offset):
                result[i][n-offset]=count
                count+=1
            for i in range(n-offset,starty,-1):
                result[n-offset][i]=count
                count+=1
            for i in range(n-offset,startx,-1):
                result[i][starty]=count
                count+=1

            offset+=1
            startx+=1
            starty+=1
        if n % 2 == 1:
            result[mid][mid] = count
        return result
