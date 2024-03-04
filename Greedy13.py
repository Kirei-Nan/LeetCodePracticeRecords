class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five=0
        ten=0
        twenty=0
        for bill in bills:
            if bill==5:
                five+=1
            if bill==10:
                ten+=1
                five-=1
            if bill==20:
                twenty+=1
                if five>0 and ten>0:
                    ten-=1
                    five-=1
                elif ten<0 and five>=3:
                    five-=3
                else:
                    return False
        return True
