# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            lth = len(queue)
            toAdd = []

            for i in range(lth):
                node = queue.popleft()
                toAdd.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            
            result.append(toAdd)

        return result


        

        
        