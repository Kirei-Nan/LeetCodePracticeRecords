# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA=lenB=0
        curA,curB=headA,headB
        while curA:
            curA=curA.next
            lenA+=1
        while curB:
            curB=curB.next
            lenB+=1
        curA, curB = headA, headB
        if lenA<lenB:
            lenA,lenB=lenB,lenA
            curA,curB=headB,headA
        for i in range(lenA-lenB):
            curA=curA.next
        while curA:
            curA=curA.next
            curB=curB.next
            if curA==curB:
                return curA
        return None