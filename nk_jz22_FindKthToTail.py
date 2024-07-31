class Solution:
    def FindKthToTail(self , pHead: ListNode, k: int) -> ListNode:
        if not pHead:
            return pHead
        slow = fast = pHead
      # 快指针先走到k-1的位置
        for i in range(0, k):
            if not fast:
                return None
            fast = fast.next
          # 快慢一起走，快走到尾节点慢正好走到倒数k节点
        while fast:
            fast = fast.next
            slow = slow.next
        return slow
