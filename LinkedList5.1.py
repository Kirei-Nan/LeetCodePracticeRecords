# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyhead=ListNode(next=head)
        cur=dummyhead
        while cur.next and cur.next.next:
            temp=cur.next
            temp2=cur.next.next.next

            cur.next=temp.next
            temp.next.next=temp
            temp.next=temp2
            cur=cur.next.next
        return dummyhead.next
