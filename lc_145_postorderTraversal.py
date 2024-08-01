# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
#递归
    # def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     res = []
    #     if not root:
    #         return res
    #     res.extend(self.postorderTraversal(root.left))
    #     res.extend(self.postorderTraversal(root.right))
    #     res.append(root.val)
    #     return res
  
#迭代
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = deque()
        prev = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if not root.right or root.right == prev:
                res.append(root.val)
                prev = root
                root = None
            else:
                stack.append(root)
                root = root.right
        return res
