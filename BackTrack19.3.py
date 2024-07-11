class Solution:
    def dfs(self,s:str,matrix:dict):
        while s in matrix and len(matrix[s])>0:
            v=matrix[s][0]
            matrix[s].pop(0)
            self.dfs(v)
            self.result.append(s)
        return self.result


    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.result=0
        tickets.sort(key=lambda x:x[1])
        matrix={}
        for i in range(len(tickets)):
            if tickets[i][0] in matrix:
                matrix[tickets[i][0]].append(tickets[i][1])
            else:
                matrix[tickets[i][0]] = [tickets[i][1]]
        for row in matrix:
            print(row)
        self.dfs("JFS",matrix)
        return self.result
