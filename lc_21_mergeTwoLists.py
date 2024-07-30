# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  # 双指针
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = head = ListNode()
        l1 = list1
        l2 = list2
        while l1 is not None or l2 is not None:
            if l2 is None:
                head.next = l1
                l1 = l1.next
            elif l1 is None:
                head.next = l2
                l2 = l2.next
            else:
                if l1.val < l2.val:
                    head.next = l1
                    l1 = l1.next
                else:
                    head.next = l2
                    l2 = l2.next
            head = head.next
        return res.next
    
