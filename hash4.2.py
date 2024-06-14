class Solution:
    def isHappy(self, n: int) -> bool:
        record = set()

        while True:
            n=self.getsum(n)
            if n==1:
                return True
            if n in record:
                return False
            else:
                record.add(n)

    def getsum(self, n: int):
        sum=0
        while n:
            k=n%10
            sum+=k**2
            n=n//10
        return sum
