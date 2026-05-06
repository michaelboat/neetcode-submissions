# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        res = [True]

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            r = dfs(node.right)
            l = dfs(node.left)

            if abs(l - r) >= 2:
                res[0] = False

            return 1 + max(l, r)

        dfs(root)
        return res[0]



        