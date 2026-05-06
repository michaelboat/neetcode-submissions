# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node:Optional[TreeNode], max_val:int) -> int:

            if not node:
                return 0

            cur = node.val

            if cur >= max_val:
                max_val = cur
                return 1 + dfs(node.left, max_val) + dfs(node.right, max_val)

            return 0 + dfs(node.left, max_val) + dfs(node.right, max_val)

        return dfs(root, root.val)

            

            

        
        