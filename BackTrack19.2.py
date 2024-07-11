class Solution:
    def backtracking(self,tickets: List[List[str]],matrix: dict,path:List[str],cur:str):
        if len(path)==len(tickets)+1:
            return path[:]

        for i in range(len(matrix[cur])):
            next_dest = matrix[cur].pop(i)
            path.append(next_dest)
            result=self.backtracking(tickets, matrix, path, next_dest)
            if result:
                return result
            path.pop()
            matrix[cur].insert(i, next_dest)

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(key=lambda x:x[1])
        matrix={}
        for i in range(len(tickets)):
            if tickets[i][0] in matrix:
                matrix[tickets[i][0]].append(tickets[i][1])
            else:
                matrix[tickets[i][0]] = [tickets[i][1]]
        for row in matrix:
            print(row)
        return self.backtracking(tickets,matrix,["JFK"],"JFK")
