# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 快慢指针找到中间节点
        if not head or not head.next:
            return True
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # 奇数需要往后移动一个节点
        if fast:
            slow = slow.next

        #翻转后半段链表
        pre = None
        while slow:
            next = slow.next
            slow.next = pre
            pre = slow
            slow = next
        
        #比较前半段和后半段链表
        fast = head
        while pre:
            if pre.val != fast.val:
                return False
            pre = pre.next
            fast = fast.next
        return True
