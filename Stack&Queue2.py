class MyQueue:

    def __init__(self):
        self.size=0
        self.in_stack=[]
        self.out_stack=[]

    def push(self, x: int) -> None:
        self.in_stack.append(x)
        self.size+=1

    def pop(self) -> int:
        if self.empty():
            return None
        self.size -= 1
        if self.out_stack:
            return self.out_stack.pop()
        else:
            for i in range(len(self.in_stack)):
                self.out_stack.append(self.in_stack.pop())
            return self.out_stack.pop()

    def peek(self) -> int:
        ans=self.pop()
        self.out_stack.append(ans)
        self.size+=1
        return ans

    def empty(self) -> bool:
        return True if self.size==0 else False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()