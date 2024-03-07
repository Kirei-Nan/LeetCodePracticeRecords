class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) < 1:
            return 0
        result=1
        points.sort(key=lambda x:x[0])
        for i in range(1,len(points)):
            if points[i][0] > points[i-1][1]:
                result+=1
            else:
                points[i][1]=min(points[i][1],points[i-1][1])
        return result
