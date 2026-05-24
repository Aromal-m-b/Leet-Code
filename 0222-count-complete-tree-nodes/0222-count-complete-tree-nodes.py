from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        res = deque([root])
        cnt = 0
        if root == None:
            return cnt
        while res:
            point = res.popleft()
            cnt += 1
            if point.left is not None:
                res.append(point.left)
            if point.right is not None:
                res.append(point.right)
        return cnt
