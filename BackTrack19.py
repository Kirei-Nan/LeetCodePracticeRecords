class Solution(object):
    def backtrack(self, tickets, path, result,cur,used):
        if len(path) == len(tickets)+1:
            result.append(path[:])
            return
        for i,ticket in enumerate(tickets):
            if ticket[0]==cur and used[i]==False:
                path.append(ticket[1])
                used[i]=True
                state=self.backtrack(tickets, path, result,ticket[1],used)
                used[i]=False
                path.pop()
                if state:
                    return

    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        result=[]
        tickets.sort()
        used=[False]*len(tickets)
        self.backtrack(tickets, ["JFK"],result,"JFK",used)
        return result[0]