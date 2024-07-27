# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA=lenB=0
        curA=headA
        curB=headB
        while curA:
            lenA+=1
            curA=curA.next
        while curB:
            lenB+=1
            curB=curB.next
        curA,curB=headA,headB
        if lenA<lenB:
            curA,curB=headB,headA
            lenA,lenB=lenB,lenA
        for i in range(lenA-lenB):
            curA=curA.next
        while curA:
            if curA==curB:
                return curA
            curA=curA.next
            curB=curB.next
        return None
