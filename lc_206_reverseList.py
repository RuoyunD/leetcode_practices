# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
          # 这里不可以创建新节点，会超出内存限制
        pre = None
        
        while head:
            next = head.next
            head.next = pre
            pre = head
            head = next
        return pre
        
