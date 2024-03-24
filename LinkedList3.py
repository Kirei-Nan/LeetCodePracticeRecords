class ListNode:
    def __int__(self,val=0,next=None):
        self.val=val
        self.next=next
class MyLinkedList(object):

    def __init__(self):
        self.dummyhead=ListNode()
        self.size=0


    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index<0 or index>self.size:
            return -1
        current=self.dummyhead.next
        for i in range(index):
            current=current.next
        return current.val


    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.size+=1
        self.dummyhead.next=ListNode(val,self.dummyhead.next)


    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.size+=1
        current=self.dummyhead
        while current.next:
            current=current.next
        current.next=ListNode(val)


    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index<0 or index>self.size:
            return

        current=self.dummyhead
        for i in range(index):
            current=current.next
        current.next=ListNode(val,current.next)
        self.size+=1


    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index<0 or index>self.size:
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