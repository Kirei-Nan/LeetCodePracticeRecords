class MyQueue:
    def __init__(self):
        self.stack_in = []
        self.out = []

    def push(self,x):
        self.stack_in.append(x)

    def pop(self):
        if self.empty():
            return

        if self.out:
            return self.out.pop()
        else:
            for i in range(len(self.stack_in)):
                self.out.append(self.stack_in.pop())
            return self.out.pop()
    def peek(self):
        """
        :rtype: int
        """
        result=self.pop()
        self.out.append(result)
        return result


    def empty(self):
        """
        :rtype: bool
        """
        if not self.stack_in and not self.out:
            return True
        else:
            return False

