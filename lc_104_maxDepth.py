# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
  #递归
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

  #bfs
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([root])
        depth = 0
        while queue:
            level_size = len(queue)
            for _ in range(0, level_size):
                root = queue.popleft()
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            depth += 1
        return depth
    #dfs
      def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_depth = 0
        stack = deque([(root, 1)])
        while stack:
            node, depth = stack.pop()
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
            max_depth = max(depth, max_depth)
        return max_depth
