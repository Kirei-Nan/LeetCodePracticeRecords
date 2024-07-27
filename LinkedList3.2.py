class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
class MyLinkedList:

    def __init__(self):
        self.dummy_head=ListNode()
        self.size=0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        cur=self.dummy_head.next
        for i in range(index):
            cur=cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        newhead=ListNode(val=val,next=self.dummy_head.next)
        self.dummy_head.next=newhead
        self.size+=1


    def addAtTail(self, val: int) -> None:
        cur=self.dummy_head
        while cur.next:
            cur=cur.next
        cur.next=ListNode(val=val)
        self.size+=1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index >= self.size:
            return
        cur = self.dummy_head
        for i in range(index):
            cur=cur.next
        cur.next=ListNode(val=val,next=cur.next)
        self.size+=1
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        cur = self.dummy_head
        for i in range(index):
            cur=cur.next
        cur.next=cur.next.next
        self.size-=1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
