# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def dfs(node: Optional[TreeNode], curr_max: list) -> int:
            
            if not node:
                return 0

            r =  dfs(node.right, curr_max)
            l = dfs(node.left, curr_max)

            if r + l >= curr_max[0]:
                curr_max[0] = r + l

            return 1 + max(l, r)
            
        curr_max = [0]
        dfs(root, curr_max)
        return curr_max[0]

        