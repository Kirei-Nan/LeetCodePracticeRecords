class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        cursum=0
        totalsum=0
        start=0

        for i in range(len(gas)):
            totalsum+=gas[i]-cost[i]
            cursum+=gas[i]-cost[i]
            if cursum<0:
                cursum=0
                start=i+1

        if totalsum<0:
            return -1

        return start

