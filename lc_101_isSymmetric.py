# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        return self.checkNodes(root.left, root.right)
    # 递归
    def checkNodes(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False    
        if root1.val != root2.val:
            return False
        return self.checkNodes(root1.left, root2.right) and self.checkNodes(root1.right, root2.left)
      #迭代
      def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        queue = deque([(root.left, root.right)])
        while queue:
            node1, node2 = queue.popleft()
            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            
            queue.append((node1.left, node2.right))
            queue.append((node1.right, node2.left))
        return True
