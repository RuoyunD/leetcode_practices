# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = head
        if res is None:
            return res
        while head.next != None:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
            
        return res

  #递归
  def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        head.next = self.deleteDuplicates(head.next)  # Recursively process the rest of the list
        
        if head.val == head.next.val:
            return head.next  # Skip the current node by returning head.next
        else:
            return head  # No duplicates, return the current node
