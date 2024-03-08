class Solution(object):
    def checknum(self,num):
        pre=float('inf')
        while num:
            digit=num % 10
            if digit <= pre:
                pre=digit
            else:
                return False
            num=num//10
        return True
    def monotoneIncreasingDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in range(n,-1,-1):
            if self.checknum(i):
                return i