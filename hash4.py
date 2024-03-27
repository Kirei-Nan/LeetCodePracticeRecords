class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        record=set()
        while True:
            sum = 0
            while n:
                digit = n % 10
                n = n // 10
                sum += digit ** 2
            n=sum

            if sum==1:
                return True
            if sum in record:
                return False
            else:
                record.add(sum)


