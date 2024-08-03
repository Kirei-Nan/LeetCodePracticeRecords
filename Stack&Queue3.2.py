class MyStack:

    def __init__(self):
        self.queuein=[]
        self.queueout=[]
    def push(self, x: int) -> None:
        self.queuein.append(x)

    def pop(self) -> int:
        if self.empty():
            return None

        while len(self.queuein)>1:
            self.queueout.append(self.queuein.pop(0))
        self.queuein,self.queueout=self.queueout,self.queuein
        ans=self.queueout.pop(0)
        return ans

    def top(self) -> int:
        ans=self.pop()
        self.queuein.append(ans)
        return ans

    def empty(self) -> bool:
        if self.queueout or self.queuein:
            return False
        return True

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()