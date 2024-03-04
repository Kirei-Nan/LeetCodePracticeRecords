class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        num=[1]*len(ratings)
        for i in range(len(ratings)-1):
            if ratings[i]<ratings[i+1]:
                num[i+1]=num[i+1]+1
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                num[i]=max(num[i+1]+1,num[i])
        return sum(num)