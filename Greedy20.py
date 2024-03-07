class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        result=[]
        if len(intervals)==0:
            return result
        intervals.sort(key=lambda x:x[0])
        result.append(intervals[0])
        for i in range(1, len(intervals)):
            if result[-1][1]>=intervals[i][0]:
                result[-1][1] = max(result[-1][1], intervals[i][1])
            else:
                result.append(intervals[i])
        return result