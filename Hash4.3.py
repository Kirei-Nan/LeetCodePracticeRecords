class Solution:
    def sumAllPosition(self,n):
        total=0
        while n:
            digit = n % 10
            total += digit ** 2
            n=n//10
        return total
    def isHappy(self, n: int) -> bool:
        record=set()
        current=n
        while current != 1:
            current = self.sumAllPosition(current)
            if current in record:
                return False
            else:
                record.add(current)
        return True
