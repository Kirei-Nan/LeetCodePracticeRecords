class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda x:(-x[0],x[1]))
        que=[]

        for person in people:
            que.insert(person[1],person)
        return que