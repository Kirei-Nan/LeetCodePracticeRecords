class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyhead=ListNode(0,head)
        current=fast=dummyhead
        for i in range(n+1):
            fast=fast.next
        while(fast):
            fast=fast.next
            current=current.next
        current.next=current.next.next
        return dummyhead.next