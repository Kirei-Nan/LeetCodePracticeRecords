from operator import add, sub, mul

def div(x, y):
    # 使用整数除法的向零取整方式
    return int(x / y) if x * y > 0 else -(abs(x) // abs(y))
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        map={"+":add,"-":sub,"*":mul,"/":div}
        stack=[]
        for i in range(len(tokens)):
            if tokens[i] not in {'+', '-', '*', '/'}:
                stack.append(int(tokens[i]))
            else:
                right=stack.pop()
                left=stack.pop()
                temp=map[tokens[i]](left,right)
                stack.append(temp)
        return int(stack.pop())