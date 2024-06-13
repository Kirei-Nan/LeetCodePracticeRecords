class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
class MyLinkedList:

    def __init__(self):
        self.dummyhead=ListNode()
        self.size=0

    def get(self, index: int) -> int:
        if index<0 or index>self.size:
            return -1
        current=self.dummyhead
        for i in range(index+1):
            current=current.next
        return current.val


    def addAtHead(self, val: int) -> None:
        self.dummyhead.next=ListNode(val,self.dummyhead.next)
        self.size+=1

    def addAtTail(self, val: int) -> None:
        current=self.dummyhead
        while current.next:
            current=current.next
        current.next=ListNode(val)
        self.size+=1


    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        current=self.dummyhead
        for i in range(index):
            current=current.next
        current.next=ListNode(val,current.next)
        self.size+=1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index > self.size:
            return
        current=self.dummyhead
        for i in range(index):
            current=current.next
        current.next=current.next.next
        self.size-=1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)