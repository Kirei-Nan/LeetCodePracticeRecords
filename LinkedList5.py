class Solution:
    def swapPairs(self,head):
        dummyhead=ListNode(0,head)
        current=dummyhead

        while current.next and current.next.next:
            temp1=current.next
            temp2 = current.next.next.next
            current.next=current.next.next
            temp1.next.next=temp1
            temp1.next=temp2
            current=current.next.next
        return dummyhead.next

