# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
  #让两个指针指回互相的链表，有结点便会相等
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        la = headA
        lb = headB
        while la != lb:
            if not la:
                la = headB
            else:
                la = la.next
            if not lb:
                lb = headA
            else:
                lb = lb.next
        return la
